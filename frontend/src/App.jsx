import { useState } from 'react';
import './index.css';

function App() {
  const [file, setFile] = useState(null);
  const [documentId, setDocumentId] = useState(null);
  const [question, setQuestion] = useState('');
  const [conversation, setConversation] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
    setDocumentId(null);
    setConversation([]);
  };

  const handleFileUpload = async () => {
    if (!file) {
      setError('Please select a PDF file to upload.');
      return;
    }

    setIsLoading(true);
    setError('');

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await fetch('http://127.0.0.1:8000/upload/', {
        method: 'POST',
        body: formData,
      });

      const data = await response.json();

      if (response.ok) {
        setDocumentId(data.document_id);
        setConversation([
          { role: 'system', message: `Document "${file.name}" uploaded and ready! You can now ask questions.` }
        ]);
        setFile(null); // Clear the file input
      } else {
        setError(data.detail || 'File upload failed.');
      }
    } catch (err) {
      setError('Network error: Failed to connect to the server.');
    } finally {
      setIsLoading(false);
    }
  };

  const handleQuery = async (e) => {
    e.preventDefault();
    if (!question || !documentId) {
      setError('Please upload a document and ask a question.');
      return;
    }

    setIsLoading(true);
    setError('');

    const userMessage = { role: 'user', message: question };
    setConversation(prev => [...prev, userMessage]);
    setQuestion('');

    try {
      const response = await fetch('http://127.0.0.1:8000/query/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ document_id: documentId, question }),
      });

      const data = await response.json();

      if (response.ok) {
        const aiMessage = { role: 'ai', message: data.answer };
        setConversation(prev => [...prev, aiMessage]);
      } else {
        setError(data.detail || 'Query failed.');
        const errorMessage = { role: 'ai', message: `Error: ${data.detail || 'Query failed.'}` };
        setConversation(prev => [...prev, errorMessage]);
      }
    } catch (err) {
      setError('Network error: Failed to get a response from the server.');
      const errorMessage = { role: 'ai', message: 'Error: Failed to get a response from the server.' };
      setConversation(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="flex flex-col h-screen bg-gray-100 font-sans">
      <header className="bg-white shadow p-4 text-center">
        <h1 className="text-2xl font-bold text-gray-800">IntelliLearn 🧠</h1>
      </header>

      <main className="flex flex-col flex-1 p-4 overflow-y-auto">
        <div className="w-full max-w-2xl mx-auto flex-1 flex flex-col">
          {error && <div className="bg-red-100 text-red-700 p-3 rounded mb-4">{error}</div>}

          {/* Upload Section */}
          <div className="bg-white shadow-md rounded-lg p-6 mb-4">
            <h2 className="text-xl font-semibold mb-2">1. Upload Document</h2>
            <input 
              type="file" 
              accept=".pdf" 
              onChange={handleFileChange} 
              className="mb-4 block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100"
            />
            <button 
              onClick={handleFileUpload} 
              disabled={!file || isLoading}
              className={`w-full py-2 px-4 rounded-md text-white font-semibold transition-colors ${!file || isLoading ? 'bg-gray-400' : 'bg-blue-600 hover:bg-blue-700'}`}
            >
              {isLoading && !documentId ? 'Uploading...' : 'Upload & Process'}
            </button>
            {documentId && (
              <p className="mt-2 text-sm text-green-600">Document successfully processed! You can now ask questions.</p>
            )}
          </div>

          {/* Chat Section */}
          <div className="bg-white shadow-md rounded-lg p-6 flex-1 flex flex-col">
            <h2 className="text-xl font-semibold mb-4">2. Chat with your AI Tutor</h2>
            <div className="flex-1 overflow-y-auto space-y-4 mb-4">
              {conversation.map((msg, index) => (
                <div key={index} className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}>
                  <div className={`p-3 rounded-lg max-w-[80%] ${msg.role === 'user' ? 'bg-blue-100 text-blue-800' : 'bg-gray-200 text-gray-800'}`}>
                    {msg.message}
                  </div>
                </div>
              ))}
            </div>

            <form onSubmit={handleQuery} className="flex space-x-2">
              <input 
                type="text"
                value={question}
                onChange={(e) => setQuestion(e.target.value)}
                disabled={!documentId || isLoading}
                placeholder={!documentId ? "Upload a document first" : "Ask a question about the document..."}
                className="flex-1 p-3 rounded-md border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
              <button
                type="submit"
                disabled={!documentId || isLoading || !question}
                className={`py-3 px-6 rounded-md text-white font-semibold transition-colors ${!documentId || isLoading || !question ? 'bg-gray-400' : 'bg-blue-600 hover:bg-blue-700'}`}
              >
                {isLoading && documentId ? 'Thinking...' : 'Send'}
              </button>
            </form>
          </div>
        </div>
      </main>
    </div>
  );
}

export default App;