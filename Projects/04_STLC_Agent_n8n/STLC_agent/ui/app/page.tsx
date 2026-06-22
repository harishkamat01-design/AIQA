'use client';

import { useState, type FormEvent } from 'react';

type FileLink = {
  name: string;
  url: string;
};

const initialState = {
  status: 'idle',
  message: 'Upload a PRD PDF to generate a test plan, test cases, and Playwright tests.',
  files: [] as Array<FileLink>
};

export default function Home() {
  const [status, setStatus] = useState(initialState.status);
  const [message, setMessage] = useState(initialState.message);
  const [files, setFiles] = useState(initialState.files);
  const [isSubmitting, setIsSubmitting] = useState(false);

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const formData = new FormData(event.currentTarget);
    const file = formData.get('prd_pdf') as File | null;

    if (!file) {
      setStatus('error');
      setMessage('Please upload a PRD PDF before submitting.');
      return;
    }

    setIsSubmitting(true);
    setStatus('loading');
    setMessage('Uploading PRD and generating artifacts...');
    setFiles([]);

    try {
      const response = await fetch('/api/submit', {
        method: 'POST',
        body: formData
      });

      if (!response.ok) {
        const body = await response.json();
        throw new Error(body?.error || 'Failed to submit the PDF.');
      }

      const result = await response.json();
      setStatus('success');
      setMessage('Artifacts generated successfully. Download them below.');
      setFiles(result.files || []);
    } catch (error) {
      console.error(error);
      setStatus('error');
      setMessage(
        error instanceof Error
          ? error.message
          : 'Unexpected error while generating artifacts.'
      );
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <main className="container">
      <section className="hero">
        <h1>STLC Agent</h1>
        <p>
          Upload your PRD PDF and generate a test plan, CSV test cases, and Playwright
          automation specs via n8n.
        </p>
      </section>

      <section className="upload-panel">
        <form onSubmit={handleSubmit} className="form-card">
          <label htmlFor="prd_pdf">Upload PRD PDF</label>
          <input type="file" id="prd_pdf" name="prd_pdf" accept="application/pdf" required />
          <button type="submit" disabled={isSubmitting}>
            {isSubmitting ? 'Generating artifacts...' : 'Generate Artifacts'}
          </button>
        </form>

        <div className="status-card">
          <p className={`status ${status}`}>{message}</p>
          {status === 'success' && files.length > 0 && (
            <div className="downloads">
              <h2>Download Files</h2>
              <ul>
                {files.map((file) => (
                  <li key={file.name}>
                    <a href={file.url} target="_blank" rel="noreferrer">
                      {file.name}
                    </a>
                  </li>
                ))}
              </ul>
            </div>
          )}
        </div>
      </section>

      <style jsx>{`
        .container {
          max-width: 960px;
          margin: 0 auto;
          padding: 3rem 1.5rem;
          font-family: Inter, system-ui, sans-serif;
        }
        .hero {
          text-align: center;
          margin-bottom: 2rem;
        }
        h1 {
          font-size: clamp(2.5rem, 5vw, 4rem);
          margin-bottom: 0.5rem;
        }
        p {
          color: #555;
          line-height: 1.8;
        }
        .upload-panel {
          display: grid;
          gap: 1.5rem;
        }
        .form-card,
        .status-card {
          background: #fff;
          border: 1px solid #e6e8eb;
          border-radius: 24px;
          padding: 2rem;
          box-shadow: 0 20px 80px rgba(16, 24, 40, 0.08);
        }
        label {
          display: block;
          margin-bottom: 0.75rem;
          color: #111827;
          font-weight: 600;
        }
        input[type='file'] {
          width: 100%;
          padding: 0.9rem 1rem;
          border: 1px solid #d1d5db;
          border-radius: 14px;
          margin-bottom: 1.25rem;
          font-size: 0.95rem;
        }
        button {
          width: 100%;
          padding: 1rem 1.1rem;
          border: none;
          border-radius: 14px;
          background: #4f46e5;
          color: white;
          font-size: 1rem;
          font-weight: 700;
          cursor: pointer;
          transition: background 0.2s ease;
        }
        button:disabled {
          background: #a5b4fc;
          cursor: not-allowed;
        }
        .status {
          font-size: 1rem;
          margin: 0;
        }
        .status.success {
          color: #166534;
        }
        .status.error {
          color: #b91c1c;
        }
        .status.loading {
          color: #0f172a;
        }
        .downloads ul {
          list-style: none;
          padding: 0;
          margin: 1rem 0 0;
        }
        .downloads li {
          margin-bottom: 0.85rem;
        }
        .downloads a {
          color: #3730a3;
          text-decoration: none;
          font-weight: 600;
        }
        .downloads a:hover {
          text-decoration: underline;
        }
        @media (min-width: 768px) {
          .upload-panel {
            grid-template-columns: 1fr 1fr;
          }
        }
      `}</style>
    </main>
  );
}
