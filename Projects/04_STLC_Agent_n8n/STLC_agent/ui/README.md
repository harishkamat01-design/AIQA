# STLC Agent UI

A production-ready React UI built with Next.js for Vercel deployment.

## Features

- PRD PDF upload
- n8n webhook integration proxy via serverless API route
- download-ready results panel
- modern responsive UI

## Deployment

1. Install dependencies:

```bash
cd ui
npm install
```

2. Set the n8n workflow webhook URL:

Create a `.env` file in `ui` with:

```bash
N8N_WEBHOOK_URL=https://YOUR_N8N_WORKFLOW_WEBHOOK_URL
```

3. Run locally:

```bash
npm run dev
```

4. Deploy to Vercel:

- Use the Vercel Dashboard and point to the `ui` folder,
- or run `vercel` from `STLC_agent/ui`.

## Notes

- The UI forwards uploads to the configured `N8N_WEBHOOK_URL`.
- Make sure the n8n workflow accepts a file field named `prd_pdf`.
