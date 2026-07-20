from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests, os
from dotenv import load_dotenv
from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer, CrossEncoder

# Load environment variables
load_dotenv()

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

# Initialize Qdrant + embedding + reranker
qdrant = QdrantClient(url=os.getenv("QDRANT_URL"))
embed_model = SentenceTransformer(os.getenv("EMBED_MODEL", "BAAI/bge-m3"))
rerank_model = CrossEncoder(os.getenv("RERANK_MODEL", "BAAI/bge-reranker-v2-m3"))

@app.post("/rag")
def rag_chat(req: ChatRequest):
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    LLM_BASE_URL = os.getenv("LLM_BASE_URL")
    LLM_MODEL = os.getenv("LLM_MODEL")
    QDRANT_COLLECTION = os.getenv("QDRANT_COLLECTION")

    if not all([GROQ_API_KEY, LLM_BASE_URL, LLM_MODEL, QDRANT_COLLECTION]):
        raise HTTPException(status_code=500, detail="Missing environment variables")

    # Step 1: Embed query
    query_vector = embed_model.encode(req.message).tolist()

    # Step 2: Retrieve candidates from Qdrant
    search_results = qdrant.search(
        collection_name=QDRANT_COLLECTION,
        query_vector=query_vector,
        limit=int(os.getenv("TOP_N_HYBRID", 20))
    )

    # Step 3: Rerank candidates
    pairs = [(req.message, hit.payload.get("text", "")) for hit in search_results]
    scores = rerank_model.predict(pairs)
    reranked = sorted(zip(search_results, scores), key=lambda x: x[1], reverse=True)
    top_hits = reranked[:int(os.getenv("TOP_K_RERANK", 4))]

    # Step 4: Build context
    context = "\n\n".join([hit.payload.get("text", "") for hit, _ in top_hits])

    # Step 5: Send contextual prompt to Groq
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": LLM_MODEL,
        "messages": [
            {"role": "system", "content": "You are a QA assistant using retrieved context."},
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion:\n{req.message}"}
        ]
    }

    try:
        response = requests.post(f"{LLM_BASE_URL}/chat/completions", headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        return {
            "answer": data["choices"][0]["message"]["content"],
            "context_used": context
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
