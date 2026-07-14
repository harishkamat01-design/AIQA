import json
import os
import threading
import time
from pathlib import Path

from flask import Flask, Response, jsonify, render_template, request
from dotenv import load_dotenv

from rag_core import build_index, generate_answer, rerank_results

load_dotenv(Path(__file__).with_name(".env"))

app = Flask(__name__, template_folder="templates")
PROJECT_ROOT = Path(__file__).resolve().parent
DATASET_PATH = PROJECT_ROOT / "testcases" / "vwo_test_cases.csv"

state = {
    "rows": [],
    "docs": [],
    "index": None,
    "dataset_path": str(DATASET_PATH),
    "ingest_events": [],
}


@app.before_request
def initialize_state():
    if state["index"] is None:
        if DATASET_PATH.exists():
            state.update(build_index(str(DATASET_PATH)))
        else:
            state["rows"] = []
            state["docs"] = []
            state["index"] = None


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/explainer")
def explainer():
    return render_template("explainer.html")


@app.get("/health")
def health():
    return jsonify({"status": "ok", "rows": len(state["rows"]), "dataset": state["dataset_path"]})


@app.post("/api/ingest")
def ingest():
    uploaded_file = request.files.get("file")
    if uploaded_file and uploaded_file.filename:
        target_path = PROJECT_ROOT / "testcases" / uploaded_file.filename
        uploaded_file.save(target_path)
        state["dataset_path"] = str(target_path)
    if not Path(state["dataset_path"]).exists():
        return jsonify({"ok": False, "error": "No dataset found"}), 400

    state["ingest_events"] = []
    def run_ingest():
        state["ingest_events"].append({"stage": "Read", "message": "Loaded CSV rows"})
        time.sleep(0.3)
        state["ingest_events"].append({"stage": "Build docs", "message": "Prepared text and metadata"})
        time.sleep(0.3)
        state["ingest_events"].append({"stage": "Chunk", "message": "Split rows into document chunks"})
        time.sleep(0.3)
        state.update(build_index(state["dataset_path"]))
        state["ingest_events"].append({"stage": "Index", "message": f"Indexed {len(state['rows'])} rows"})

    thread = threading.Thread(target=run_ingest, daemon=True)
    thread.start()
    return jsonify({"ok": True, "dataset": state["dataset_path"]})


@app.get("/api/ingest-progress")
def ingest_progress():
    def stream():
        last_count = -1
        while True:
            current = state["ingest_events"]
            if len(current) != last_count:
                last_count = len(current)
                yield f"data: {json.dumps({'events': current})}\n\n"
            if len(current) >= 4:
                break
            time.sleep(0.2)
    return Response(stream(), mimetype="text/event-stream")


@app.get("/api/chunks")
def chunks():
    if state["index"] is None:
        return jsonify({"chunks": []})

    page = max(int(request.args.get("page", 1)), 1)
    per_page = min(max(int(request.args.get("per_page", 20)), 1), 100)
    search = request.args.get("search", "").strip().lower()
    priority = request.args.get("priority", "").strip()
    module = request.args.get("module", "").strip()
    jira_id = request.args.get("jira_id", "").strip()

    filtered = []
    for item in state["docs"]:
        meta = item["meta"]
        text = item["text"].lower()
        if search and search not in text:
            continue
        if priority and str(meta.get("priority", "")).lower() != priority.lower():
            continue
        if module and str(meta.get("module", "")).lower() != module.lower():
            continue
        if jira_id and str(meta.get("jira_id", "")).lower() != jira_id.lower():
            continue
        filtered.append(item)

    start = (page - 1) * per_page
    end = start + per_page
    return jsonify({
        "chunks": filtered[start:end],
        "page": page,
        "per_page": per_page,
        "total": len(filtered),
    })


@app.post("/api/chat")
def chat():
    if state["index"] is None:
        return jsonify({"error": "No index available"}), 400

    payload = request.get_json(silent=True) or {}
    question = (payload.get("question") or "").strip()
    if not question:
        return jsonify({"error": "Please enter a question"}), 400

    hits, detail_rows = rerank_results(question, state["index"])
    answer = generate_answer(question, hits)
    return jsonify({
        "question": question,
        "rewrites": detail_rows,
        "hits": hits,
        "answer": answer,
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5050")), debug=True)
