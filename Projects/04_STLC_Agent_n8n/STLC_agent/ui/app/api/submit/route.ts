import { NextRequest, NextResponse } from 'next/server';

export async function POST(request: NextRequest) {
  const webhookUrl = process.env.N8N_WEBHOOK_URL;

  if (!webhookUrl) {
    return NextResponse.json(
      { error: 'N8N_WEBHOOK_URL is not configured.' },
      { status: 500 }
    );
  }

  const formData = await request.formData();
  const file = formData.get('prd_pdf');

  if (!file || !(file instanceof File)) {
    return NextResponse.json({ error: 'Invalid PDF upload.' }, { status: 400 });
  }

  const forwarded = new FormData();
  forwarded.append('prd_pdf', file, file.name);

  try {
    const response = await fetch(webhookUrl, {
      method: 'POST',
      body: forwarded
    });

    if (!response.ok) {
      const payload = await response.text();
      return NextResponse.json(
        { error: 'n8n webhook request failed.', details: payload },
        { status: response.status }
      );
    }

    const result = await response.json();

    if (!Array.isArray(result.files)) {
      return NextResponse.json(
        { error: 'Invalid response from n8n workflow.' },
        { status: 502 }
      );
    }

    return NextResponse.json({ files: result.files });
  } catch (error) {
    return NextResponse.json(
      { error: error instanceof Error ? error.message : 'Unknown error' },
      { status: 500 }
    );
  }
}
