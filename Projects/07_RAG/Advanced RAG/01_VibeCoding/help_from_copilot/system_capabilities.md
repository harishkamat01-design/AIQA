Your Current System Capabilities

Area	     Availability	                 Description

Environment	✅ Python 3.12 + VS Code	        You can run virtual environments and manage dependencies locally.
Model Layer	✅ bge‑m3 + bge‑reranker‑v2‑m3	Dense + sparse hybrid retrieval and cross‑encoder reranking are supported.
Vector DB	✅ Qdrant (Docker or embedded)	You can run Qdrant either as a local Docker container or embedded file store.
LLM Layer	✅ Groq openai/gpt‑oss‑120b	    Handles generation and query rewriting.
Pipeline	✅ Ingestion + Chat stages	   CSV/XLSX ingestion, chunking, embedding, indexing, and live chat retrieval.
UI Layer	✅ Atlassian‑style two‑pane layout	Left: pipeline tracker; Right: active content/chat.
Automation	✅ CLI ingestion	Supports structured test‑case ingestion via command line.
Data Store	✅ Local /testcases folder	     Stores 5 000 VWO test cases in CSV (JIRA format).
Docs & Visualization	✅ Markdown + HTML	  You can generate animated HTML documentation explaining your RAG architecture.