import type { Metadata } from 'next';
import './globals.css';

export const metadata: Metadata = {
  title: 'STLC Agent',
  description: 'Upload a PRD PDF and generate QA artifacts using n8n.',
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
