# IntelliLearn: AI-Powered Personalized Knowledge Base 🎓

IntelliLearn is a full-stack application that transforms static PDF documents into interactive, searchable knowledge bases. Using **Retrieval-Augmented Generation (RAG)**, the app allows users to upload documents and have natural language conversations with an AI grounded in the specific context of those files.

---

## 🚀 Features

* **Document Ingestion:** Seamlessly upload PDF files via a React-based frontend.
* **Semantic Search:** Uses vector embeddings to understand the meaning of queries rather than just matching keywords.
* **Context-Aware Responses:** Leverages OpenAI's GPT models to provide answers based strictly on the uploaded content.
* **Vector Storage:** Utilizes **ChromaDB** for efficient storage and retrieval of high-dimensional document vectors.
* **Modern UI:** Responsive and clean interface built with **Tailwind CSS**.

---

## 🛠️ Tech Stack

| Component        | Technology                           |
| ---------------- | ------------------------------------ |
| **Frontend**     | React.js, Tailwind CSS, Lucide React |
| **Backend**      | FastAPI (Python), Uvicorn            |
| **AI Framework** | LangChain                            |
| **LLM**          | OpenAI (GPT-3.5-Turbo-Instruct)      |
| **Embeddings**   | HuggingFace (`all-MiniLM-L6-v2`)     |
| **Vector DB**    | ChromaDB                             |

---

## 🏗️ How It Works (RAG Pipeline)

1. **Preprocessing:**

   * PDF text is extracted and split into 1,000-character chunks with a 200-character overlap to preserve context.

2. **Embedding:**

   * Text chunks are converted into 384-dimensional numerical vectors using `all-MiniLM-L6-v2`.

3. **Retrieval:**

   * When a question is asked, the system performs a semantic search in **ChromaDB** to find the most relevant chunks.

4. **Generation:**

   * The retrieved context and user question are sent to the OpenAI LLM to generate a factual, grounded response.

---

## 📂 Project Structure

```
IntelliLearn/
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   ├── services/
│   │   ├── ingestion.py
│   │   ├── retrieval.py
│   │   └── generation.py
│   └── .env
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   └── App.jsx
│   ├── package.json
│   └── tailwind.config.js
│
├── uploads/          # Stored uploaded PDF files
├── chromadb/         # Persistent vector database storage
│
└── README.md
```

IntelliLearn/
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   ├── services/
│   │   ├── ingestion.py
│   │   ├── retrieval.py
│   │   └── generation.py
│   └── .env
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   └── App.jsx
│   ├── package.json
│   └── tailwind.config.js
│
└── README.md

````

---

## 🚦 Getting Started

### 1. Prerequisites

- Python 3.10+
- Node.js & npm
- OpenAI API Key

---

### 2. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create a .env file and add your key
echo 'OPENAI_API_KEY="your_actual_key_here"' > .env

# Install dependencies
pip install -r requirements.txt

# Start the server
python -m uvicorn main:app --reload
````

---

### 3. Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Run the development server
npm run dev
```

---

## 🔗 API Endpoints (Example)

| Method | Endpoint  | Description                            |
| ------ | --------- | -------------------------------------- |
| POST   | `/upload` | Upload PDF and process embeddings      |
| POST   | `/query`  | Ask questions about uploaded documents |

---

## 🧠 Example Workflow

1. Upload a PDF document.
2. The system processes and stores embeddings.
3. Ask a question in natural language.
4. Receive a context-aware answer grounded in your document.

---

## ⚡ Future Improvements

* Multi-document querying
* User authentication and document management
* Streaming responses for better UX
* Support for additional file types (DOCX, TXT, HTML)
* Hybrid search (keyword + semantic)

---

## 🤝 Contributing

Contributions are welcome. Please fork the repository and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 💡 Acknowledgements

* OpenAI
* HuggingFace
* LangChain
* ChromaDB

---

## ⭐ Support

If you found this project useful, consider giving it a star on GitHub.
