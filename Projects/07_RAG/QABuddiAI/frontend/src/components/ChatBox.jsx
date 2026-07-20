import { useState } from "react";
import { askRag } from "../api/rag";

export default function ChatBox() {
  const [input, setInput] = useState("");
  const [answer, setAnswer] = useState("");
  const [context, setContext] = useState("");

  const handleAsk = async () => {
    try {
      const result = await askRag(input);
      setAnswer(result.answer);
      setContext(result.context_used);
    } catch (err) {
      setAnswer("Error fetching answer: " + err.message);
    }
  };

  return (
    <div className="p-6 max-w-2xl mx-auto">
      <textarea
        className="w-full border rounded p-2 mb-4"
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Ask about a test case..."
      />
      <button
        className="bg-blue-600 text-white px-4 py-2 rounded"
        onClick={handleAsk}
      >
        Ask QA Buddy
      </button>

      {answer && (
        <div className="mt-6">
          <h2 className="text-lg font-bold">Answer</h2>
          <p className="bg-gray-100 p-3 rounded">{answer}</p>

          <h3 className="text-md font-semibold mt-4">Context Used</h3>
          <pre className="bg-gray-50 p-3 rounded text-sm whitespace-pre-wrap">
            {context}
          </pre>
        </div>
      )}
    </div>
  );
}
