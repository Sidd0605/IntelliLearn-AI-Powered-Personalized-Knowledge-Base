# # import os
# # import shutil
# # import uuid
# # from pathlib import Path
# # from fastapi import FastAPI, UploadFile, File, HTTPException
# # from pydantic import BaseModel
# # from typing import Dict
# # from .rag_engine import get_or_create_vector_store, get_rag_chain
# # from fastapi.middleware.cors import CORSMiddleware

# # # Initialize FastAPI
# # app = FastAPI(title="IntelliLearn API")
# # # Add CORS middleware
# # origins = [
# #     "http://localhost",
# #     "http://localhost:5173",  # Your frontend's origin
# # ]

# # app.add_middleware(
# #     CORSMiddleware,
# #     allow_origins=origins,
# #     allow_credentials=True,
# #     allow_methods=["*"],
# #     allow_headers=["*"],
# # )

# # # Define a directory to store uploaded files
# # UPLOAD_DIR = Path("uploads")
# # UPLOAD_DIR.mkdir(exist_ok=True)

# # # A simple in-memory store for document metadata
# # # In a real app, this would be a database like PostgreSQL
# # doc_metadata_db: Dict[str, str] = {}

# # class QueryRequest(BaseModel):
# #     document_id: str
# #     question: str

# # @app.get("/")
# # async def read_root():
# #     return {"message": "Welcome to the IntelliLearn API! Go to /docs for API documentation."}

# # @app.post("/upload/")
# # async def upload_document(file: UploadFile = File(...)):
# #     """
# #     Handles PDF file uploads, saves the file, and initializes a ChromaDB collection.
# #     """
# #     if file.content_type != "application/pdf":
# #         raise HTTPException(status_code=400, detail="Invalid file type. Only PDF files are allowed.")

# #     # Create a unique ID for the document
# #     document_id = str(uuid.uuid4())
# #     file_path = UPLOAD_DIR / f"{document_id}.pdf"
    
# #     # Save the file to disk
# #     with open(file_path, "wb") as buffer:
# #         shutil.copyfileobj(file.file, buffer)

# #     # Initialize the RAG pipeline for this document in the background
# #     try:
# #         get_or_create_vector_store(str(file_path), document_id)
# #         doc_metadata_db[document_id] = file.filename
# #         return {"document_id": document_id, "message": "File uploaded and processing started."}
# #     except Exception as e:
# #         # Clean up the file if processing fails
# #         os.remove(file_path)
# #         raise HTTPException(status_code=500, detail=f"Failed to process document: {str(e)}")

# # @app.post("/query/")
# # async def process_query(request: QueryRequest):
# #     """
# #     Receives a user query and returns a RAG-based answer.
# #     """
# #     # Check if the document exists in our simple database
# #     if request.document_id not in doc_metadata_db:
# #         raise HTTPException(status_code=404, detail="Document not found.")

# #     try:
# #         # Get the file path and vector store instance for the document
# #         file_path = UPLOAD_DIR / f"{request.document_id}.pdf"
# #         vector_store = get_or_create_vector_store(str(file_path), request.document_id)
        
# #         # Get the RAG chain and run the query
# #         rag_chain = get_rag_chain(vector_store)
# #         response = rag_chain.invoke({"input": request.question})
        
# #         return {"answer": response['answer']}
# #     except Exception as e:
# #         raise HTTPException(status_code=500, detail=f"Failed to process query: {str(e)}")

# import os
# import shutil
# import uuid
# from pathlib import Path
# from fastapi import FastAPI, UploadFile, File, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
# from typing import Dict
# from .rag_engine import get_or_create_vector_store, get_rag_chain

# # Initialize FastAPI
# app = FastAPI(title="IntelliLearn API")

# # Add CORS middleware
# origins = [
#     "http://localhost",
#     "http://localhost:5173",
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Define a directory to store uploaded files
# UPLOAD_DIR = Path("uploads")
# UPLOAD_DIR.mkdir(exist_ok=True)

# doc_metadata_db: Dict[str, str] = {}

# class QueryRequest(BaseModel):
#     document_id: str
#     question: str

# @app.get("/")
# async def read_root():
#     return {"message": "Welcome to the IntelliLearn API! Go to /docs for API documentation."}

# @app.post("/upload/")
# async def upload_document(file: UploadFile = File(...)):
#     """
#     Handles PDF file uploads, saves the file, and initializes a ChromaDB collection.
#     """
#     if file.content_type != "application/pdf":
#         raise HTTPException(status_code=400, detail="Invalid file type. Only PDF files are allowed.")

#     document_id = str(uuid.uuid4())
#     file_path = UPLOAD_DIR / f"{document_id}.pdf"
    
#     with open(file_path, "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)

#     try:
#         get_or_create_vector_store(str(file_path), document_id)
#         doc_metadata_db[document_id] = file.filename
#         return {"document_id": document_id, "message": "File uploaded and processing started."}
#     except Exception as e:
#         os.remove(file_path)
#         raise HTTPException(status_code=500, detail=f"Failed to process document: {str(e)}")

# # @app.post("/query/")
# # async def process_query(request: QueryRequest):
# #     """
# #     Receives a user query and returns a RAG-based answer.
# #     """
# #     if request.document_id not in doc_metadata_db:
# #         raise HTTPException(status_code=404, detail="Document not found.")

# #     try:
# #         file_path = UPLOAD_DIR / f"{request.document_id}.pdf"
# #         vector_store = get_or_create_vector_store(str(file_path), request.document_id)
        
# #         rag_chain = get_rag_chain(vector_store)
# #         response = rag_chain.invoke({"input": request.question})
        
# #         return {"answer": response['answer']}
# #     except Exception as e:
# #         raise HTTPException(status_code=500, detail=f"Failed to process query: {str(e)}")

# @app.post("/query/")
# async def process_query(request: QueryRequest):
#     if request.document_id not in doc_metadata_db:
#         raise HTTPException(status_code=404, detail="Document not found.")

#     try:
#         file_path = UPLOAD_DIR / f"{request.document_id}.pdf"
#         vector_store = get_or_create_vector_store(str(file_path), request.document_id)
        
#         rag_chain = get_rag_chain(vector_store)
#         response = rag_chain.invoke({"input": request.question})

#         # 👇 Add this line for debugging
#         print("RAG Response:", response)

#         if isinstance(response, dict):
#             return {
#                 "answer": response.get("answer") or response.get("output") or str(response)
#             }
#         else:
#             return {"answer": str(response)}

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Failed to process query: {str(e)}")



import os
from pathlib import Path
from dotenv import load_dotenv

# -----------------------------
# Load .env before any LangChain imports
# -----------------------------
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

# Debug print (optional)
print("OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))
print("OPENAI_API_BASE:", os.getenv("OPENAI_API_BASE"))

import shutil
import uuid
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict
# from rag_engine import get_or_create_vector_store, get_rag_chain
from .rag_engine import get_or_create_vector_store, get_rag_chain

# -----------------------------
# FastAPI setup
# -----------------------------
app = FastAPI(title="IntelliLearn API")

origins = ["http://localhost", "http://localhost:5173"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

doc_metadata_db: Dict[str, str] = {}

class QueryRequest(BaseModel):
    document_id: str
    question: str

# -----------------------------
# Endpoints
# -----------------------------
@app.get("/")
async def read_root():
    return {"message": "Welcome to the IntelliLearn API! Go to /docs for API documentation."}

@app.post("/upload/")
async def upload_document(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files allowed.")

    document_id = str(uuid.uuid4())
    file_path = UPLOAD_DIR / f"{document_id}.pdf"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        get_or_create_vector_store(str(file_path), document_id)
        doc_metadata_db[document_id] = file.filename
        return {"document_id": document_id, "message": "File uploaded and processing started."}
    except Exception as e:
        os.remove(file_path)
        raise HTTPException(status_code=500, detail=f"Failed to process document: {str(e)}")

@app.post("/query/")
async def process_query(request: QueryRequest):
    if request.document_id not in doc_metadata_db:
        raise HTTPException(status_code=404, detail="Document not found.")

    try:
        file_path = UPLOAD_DIR / f"{request.document_id}.pdf"
        vector_store = get_or_create_vector_store(str(file_path), request.document_id)

        rag_chain = get_rag_chain(vector_store)
        response = rag_chain.invoke({"input": request.question})

        # Safely get answer
        if isinstance(response, dict):
            answer = response.get("answer") or response.get("output") or str(response)
        else:
            answer = str(response)

        return {"answer": answer}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to process query: {str(e)}")

