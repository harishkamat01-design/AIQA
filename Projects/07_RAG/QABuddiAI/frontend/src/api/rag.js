export async function askRag(message) {
  const response = await fetch('/rag', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message }),
  });
  if (!response.ok) throw new Error(`Error: ${response.statusText}`);
  return await response.json();
}
