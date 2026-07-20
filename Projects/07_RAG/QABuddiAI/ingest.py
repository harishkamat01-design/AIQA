import pandas as pd
from qdrant_client import QdrantClient
from qdrant_client.http import models
from sentence_transformers import SentenceTransformer
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

QDRANT_URL = os.getenv("QDRANT_URL", "http://localhost:6333")
QDRANT_COLLECTION = os.getenv("QDRANT_COLLECTION", "vwo_test_cases")
EMBED_MODEL = os.getenv("EMBED_MODEL", "BAAI/bge-m3")

# Initialize clients
qdrant = QdrantClient(url=QDRANT_URL)
embed_model = SentenceTransformer(EMBED_MODEL)

# Load CSV
df = pd.read_csv("testcases/vwo_test_cases.csv")

# ✅ Create collection safely (no deprecation warnings)
if not qdrant.collection_exists(QDRANT_COLLECTION):
    qdrant.create_collection(
        collection_name=QDRANT_COLLECTION,
        vectors_config=models.VectorParams(
            size=embed_model.get_embedding_dimension(),  # updated method name
            distance=models.Distance.COSINE
        ),
    )

# Ingest rows
points = []
for idx, row in df.iterrows():
    text = f"{row['title']} {row['steps']} {row['expected']} {row['tags']}"
    vector = embed_model.encode(text, batch_size=4).tolist()  # safer batch size
    payload = {
        "id": int(row["id"]),
        "jira_id": row["jira_id"],
        "priority": row["priority"],
        "module": row["module"],
        "title": row["title"],
        "steps": row["steps"],
        "expected": row["expected"],
        "tags": row["tags"],
        "text": text
    }
    points.append(models.PointStruct(id=int(row["id"]), vector=vector, payload=payload))

qdrant.upsert(collection_name=QDRANT_COLLECTION, points=points)

print(f"Ingested {len(points)} test cases into Qdrant collection '{QDRANT_COLLECTION}'")
