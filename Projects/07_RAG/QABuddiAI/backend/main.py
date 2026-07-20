from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Query(BaseModel):
    message: str

@app.post("/rag")
async def rag_endpoint(query: Query):
    # For now, just echo back the message
    return {
        "answer": f"You asked: {query.message}",
        "context_used": "Demo context from backend"
    }


