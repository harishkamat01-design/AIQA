import json
import os
import re
import urllib.request
from typing import Any, Dict, List

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


DEFAULT_CHUNK_SIZE = 1000
DEFAULT_CHUNK_OVERLAP = 150
DEFAULT_TOP_N_HYBRID = 20
DEFAULT_TOP_K_RERANK = 4
DEFAULT_RRF_K = 60
DEFAULT_REWRITE_ENABLED = True


def normalize_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text or "")
    return text.strip()


def make_doc_text(row: Dict[str, Any]) -> str:
    title = normalize_text(str(row.get("title", "")))
    steps = normalize_text(str(row.get("steps", "")))
    expected = normalize_text(str(row.get("expected", "")))
    tags = normalize_text(str(row.get("tags", "")))
    return f"Title: {title}\nSteps: {steps}\nExpected: {expected}\nTags: {tags}"


def build_docs(rows: List[Dict[str, Any]], chunk_size: int = DEFAULT_CHUNK_SIZE, overlap: int = DEFAULT_CHUNK_OVERLAP) -> List[Dict[str, Any]]:
    docs: List[Dict[str, Any]] = []
    for index, row in enumerate(rows):
        text = make_doc_text(row)
        meta = {
            "id": row.get("id", index + 1),
            "jira_id": row.get("jira_id", ""),
            "priority": row.get("priority", "P2"),
            "module": row.get("module", "General"),
            "title": row.get("title", ""),
            "tags": row.get("tags", ""),
        }
        docs.append({"id": index + 1, "text": text, "meta": meta})
    return docs


class RetrievalIndex:
    def __init__(self, docs: List[Dict[str, Any]]):
        self.docs = docs
        self.texts = [doc["text"] for doc in docs]
        self.vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2), min_df=1)
        self.matrix = self.vectorizer.fit_transform(self.texts)

    def dense_scores(self, query: str) -> np.ndarray:
        query_vector = self.vectorizer.transform([query])
        return cosine_similarity(query_vector, self.matrix).ravel()

    def sparse_scores(self, query: str) -> np.ndarray:
        query_tokens = set(re.findall(r"[a-z0-9]+", query.lower()))
        scores = []
        for text in self.texts:
            tokens = set(re.findall(r"[a-z0-9]+", text.lower()))
            overlap = len(query_tokens & tokens)
            scores.append(overlap)
        return np.array(scores)


def rewrite_query(query: str, enabled: bool = DEFAULT_REWRITE_ENABLED) -> List[str]:
    if not enabled:
        return [query]

    api_key = os.getenv("GROQ_API_KEY", "").strip()
    if not api_key:
        return [query, f"{query} details", f"How to handle {query}"]

    payload = {
        "model": os.getenv("GROQ_MODEL", "openai/gpt-oss-120b"),
        "temperature": 0.2,
        "messages": [
            {
                "role": "system",
                "content": "Rewrite the user's question into 3 short alternate phrasings for product test-case retrieval.",
            },
            {"role": "user", "content": query},
        ],
    }

    try:
        req = urllib.request.Request(
            "https://api.groq.com/openai/v1/chat/completions",
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {api_key}",
            },
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=20) as response:
            body = json.loads(response.read().decode("utf-8"))
            content = body.get("choices", [{}])[0].get("message", {}).get("content", "")
            rewrites = [part.strip() for part in content.split("\n") if part.strip()]
            if len(rewrites) >= 3:
                return [query] + rewrites[:3]
    except Exception:
        pass

    return [query, f"{query} in detail", f"How to solve {query}"]


def rerank_results(query: str, index: RetrievalIndex, top_n: int = DEFAULT_TOP_N_HYBRID, rerank_k: int = DEFAULT_TOP_K_RERANK, rrf_k: int = DEFAULT_RRF_K) -> List[Dict[str, Any]]:
    rewrites = rewrite_query(query)
    rank_lists: List[List[tuple[int, float]]] = []
    detail_rows: List[Dict[str, Any]] = []

    for rewrite in rewrites:
        dense = index.dense_scores(rewrite)
        sparse = index.sparse_scores(rewrite)
        dense_rank = sorted([(i, float(score)) for i, score in enumerate(dense)], key=lambda item: item[1], reverse=True)[:top_n]
        sparse_rank = sorted([(i, float(score)) for i, score in enumerate(sparse)], key=lambda item: item[1], reverse=True)[:top_n]
        rank_lists.append(dense_rank)
        rank_lists.append(sparse_rank)
        detail_rows.append({"rewrite": rewrite, "dense": dense_rank[:5], "sparse": sparse_rank[:5]})

    rrf_scores: Dict[int, float] = {}
    for ranks in rank_lists:
        for rank_position, (doc_id, _) in enumerate(ranks):
            rrf_scores[doc_id] = rrf_scores.get(doc_id, 0.0) + 1.0 / (rrf_k + rank_position + 1)

    final_hits = []
    for doc_id, score in rrf_scores.items():
        doc = index.docs[doc_id]
        lexical_bonus = len(set(re.findall(r"[a-z0-9]+", query.lower())) & set(re.findall(r"[a-z0-9]+", doc["text"].lower()))) * 0.08
        final_hits.append({
            "doc_id": doc_id,
            "score": score + lexical_bonus,
            "text": doc["text"],
            "meta": doc["meta"],
            "rank": 0,
        })

    final_hits = sorted(final_hits, key=lambda item: item["score"], reverse=True)[:rerank_k]
    for rank_position, item in enumerate(final_hits):
        item["rank"] = rank_position + 1
    return final_hits, detail_rows


def generate_answer(query: str, hits: List[Dict[str, Any]]) -> Dict[str, Any]:
    api_key = os.getenv("GROQ_API_KEY", "").strip()
    if not api_key:
        answer = "The GROQ API key is not available in the environment, so a grounded answer cannot be generated yet."
        return {"answer": answer, "model": "offline", "citations": [item["meta"]["jira_id"] for item in hits]}

    context = "\n\n---\n\n".join([f"[Chunk {item['doc_id']}] {item['text']}" for item in hits])
    payload = {
        "model": os.getenv("GROQ_MODEL", "openai/gpt-oss-120b"),
        "temperature": 0.2,
        "messages": [
            {
                "role": "system",
                "content": "You answer only using the provided context and cite the relevant chunk numbers.",
            },
            {"role": "user", "content": f"Question: {query}\n\nContext:\n{context}"},
        ],
    }

    try:
        req = urllib.request.Request(
            "https://api.groq.com/openai/v1/chat/completions",
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {api_key}",
            },
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=25) as response:
            body = json.loads(response.read().decode("utf-8"))
            answer = body.get("choices", [{}])[0].get("message", {}).get("content", "")
            return {"answer": answer, "model": payload["model"], "citations": [item["meta"]["jira_id"] for item in hits]}
    except Exception as exc:
        return {"answer": f"The retrieval pipeline completed, but GROQ returned an error: {exc}", "model": payload["model"], "citations": [item["meta"]["jira_id"] for item in hits]}


def load_csv(csv_path: str) -> List[Dict[str, Any]]:
    df = pd.read_csv(csv_path)
    rows = df.to_dict(orient="records")
    return rows


def build_index(csv_path: str) -> Dict[str, Any]:
    rows = load_csv(csv_path)
    docs = build_docs(rows)
    index = RetrievalIndex(docs)
    return {"rows": rows, "docs": docs, "index": index}
