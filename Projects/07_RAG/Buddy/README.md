# QABuddy.ai

## Overview
QABuddy.ai is a self‑hosted, hybrid Retrieval‑Augmented Generation (RAG) system that powers QA engineers with a single, cited answer.  The system ingests code, test data, JIRA tickets, documentation, and logs, indexes them in an open‑source vector database, and serves grounded answers via a chatbot.

## Folder Structure
```
Buddy/
├─ Selenium_framework_repo          # Selenium framework source
├─ Playwright_framework_repo        # Playwright framework source
├─ Test_cases                       # CSV / XLSX test data (~1,000 rows)
├─ JIRA_tickets                     # JIRA tickets (injected via MCP)
├─ Company_docs                      # PDFs / Markdown docs
├─ Figma_designs                     # ER diagrams, wireframes (Phase 2)
├─ Meeting_notes                     # Transcripts of meetings
├─ Lucid_charts                      # Text exports of Lucid charts
├─ PRD_SRS_BRD_FRD                   # PRD / SRS / BRD / FRD PDFs
├─ Jenkins_logs                      # Log / text files
└─ .env                              # Environment variables
```

## Prerequisites
| Component | Version | Notes |
|-----------|---------|-------|
| Python | 3.11+ | Used for ingestion scripts and the chatbot server |
| Node.js | 20+ | Required for running the chatbot UI |
| Docker | 24+ | Optional – for containerised deployment |
| Git | 2.30+ | For cloning the framework repos |
| JIRA | Cloud | API token required |
| GROQ | API key | For LLM inference |

## Setup Steps
1. **Clone the framework repositories**
   ```bash
   cd Buddy
   git clone https://github.com/PramodDutta/ATB13xSeleniumAdvanceFramework Selenium_framework_repo
   git clone https://github.com/PramodDutta/Advance-Playwright-Framework Playwright_framework_repo
   ```

2. **Create a virtual environment and install dependencies**
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate
   pip install -r requirements.txt
   ```
   *`requirements.txt`* should contain packages such as `langchain`, `faiss-cpu`, `pandas`, `openpyxl`, `PyPDF2`, `jira`, `groq`, etc.

3. **Configure environment variables**
   Create a file named `.env` in the root of the project (the file you already provided). It should look like this:
   ```dotenv
   GROQ_API_KEY="your_groq_key"
   JIRA_BASE_URL="https://harishkamat01-1356.atlassian.net"
   JIRA_EMAIL="harish.kamat01@gmail.com"
   JIRA_API_TOKEN="your_jira_token"
   JIRA_JQL="project = VWO ORDER BY updated DESC"
   ```
   *Replace the placeholder values with your actual keys.*

4. **Run the ingestion pipeline**
   ```bash
   python ingest.py
   ```
   The script will:
   * Parse code from the two framework repos.
   * Read test case CSV/XLSX files.
   * Pull JIRA tickets using the provided JQL.
   * Extract PDFs/Markdown from `Company_docs`.
   * Chunk, embed, and index everything into a local FAISS vector store.

5. **Start the chatbot server**
   ```bash
   python app.py
   ```
   The server will expose a REST endpoint (e.g., `http://localhost:8000/chat`).  You can interact with it via the provided UI or via `curl`.

6. **Optional – Dockerise the application**
   ```bash
   docker build -t qabaddy .
   docker run -d -p 8000:8000 --env-file .env qabaddy
   ```

## Usage
- **Ask a question**: Send a POST request to `/chat` with a JSON body `{"question": "What is the login flow?"}`.
- **Get a cited answer**: The response will include the answer text and a list of citations (file names, line numbers, or JIRA ticket IDs).

## Maintenance
- **Hourly re‑ingestion**: Set up a cron job or a systemd timer to run `python ingest.py` every hour.
- **Adding new data**: Drop new files into the appropriate source folder and re‑run the ingestion.
- **Updating embeddings**: If you change the embedding model, re‑run the ingestion to rebuild the vector store.

## Troubleshooting
| Symptom | Likely Cause | Fix |
|---------|--------------|-----|
| `ModuleNotFoundError` | Missing dependency | `pip install -r requirements.txt` |
| No answers returned | Vector store empty | Verify ingestion completed successfully |
| Authentication errors | Wrong API keys | Double‑check `.env` values |

## License
MIT © 2026 QABuddy.ai
