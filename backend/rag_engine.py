# import dotenv
# dotenv.load_dotenv()

# import os
# from langchain_community.document_loaders import PyPDFLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_community.embeddings import HuggingFaceEmbeddings
# from langchain_community.vectorstores import Chroma
# from langchain_openai import OpenAI
# from langchain.prompts import PromptTemplate
# from langchain.chains.combine_documents import create_stuff_documents_chain
# from langchain.chains import create_retrieval_chain

# os.environ["ANONYMIZED_TELEMETRY"] = "false"

# # A helper function to manage the ChromaDB instance
# def get_or_create_vector_store(file_path: str, collection_name: str) -> Chroma:
#     """
#     Loads, chunks, and embeds a PDF, then stores it in ChromaDB.
#     Returns the vector store instance.
#     """
#     # Create a unique directory for the collection's data
#     persist_directory = f"./chroma_db/{collection_name}"
    
#     # Check if a vector store for this collection already exists
#     if os.path.exists(persist_directory):
#         print(f"Loading existing vector store for '{collection_name}'...")
#         embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
#         return Chroma(
#             persist_directory=persist_directory,
#             embedding_function=embedding_model
#         )

#     print(f"Creating a new vector store for '{collection_name}'...")
#     # 1. Load the PDF document
#     loader = PyPDFLoader(file_path)
#     documents = loader.load()

#     # 2. Split documents into chunks
#     text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
#     docs = text_splitter.split_documents(documents)

#     # 3. Create embeddings and store in a new vector store
#     embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
#     vector_store = Chroma.from_documents(
#         docs, 
#         embedding_model, 
#         persist_directory=persist_directory
#     )
    
#     print(f"Vector store created for '{collection_name}'!")
#     return vector_store

# # def get_rag_chain(vector_store: Chroma):
# #     """
# #     Creates and returns a retrieval chain for answering questions.
# #     """
# #     # Initialize the LLM
# #     # Make sure to set your OpenAI API key in your environment variables
# #     # llm = OpenAI(model_name="gpt-3.5-turbo-instruct", temperature=0.7)
# #     llm = OpenAI(model_name="gpt-3.5-turbo-instruct", temperature=0.7, openai_api_key=os.getenv("OPENAI_API_KEY"))

# #     # Define the custom prompt template for RAG
# #     rag_prompt = PromptTemplate.from_template("""
# #         You are an AI assistant for a personalized knowledge base. 
# #         Use the following retrieved context to answer the question.
# #         If you cannot find the answer in the provided context, politely state that you do not have enough information to answer.
        
# #         Context:
# #         {context}
        
# #         Question:
# #         {input}
# #         """)

# #     # Create a retrieval chain with the custom prompt
# #     document_chain = create_stuff_documents_chain(llm, rag_prompt)
# #     retrieval_chain = create_retrieval_chain(vector_store.as_retriever(), document_chain)
    
# #     return retrieval_chain

# from langchain_openai import ChatOpenAI
# import os

# def get_rag_chain(vector_store):
#     llm = ChatOpenAI(
#         model="moonshotai/kimi-k2",  # OpenRouter model
#         temperature=0.7,
#         openai_api_key=os.getenv("OPENAI_API_KEY"),   # must not be None
#         openai_api_base=os.getenv("OPENAI_API_BASE", "https://openrouter.ai/api/v1"),
#     )

#     rag_prompt = PromptTemplate.from_template("""
#         You are an AI assistant...
#         Context:
#         {context}
#         Question:
#         {input}
#     """)

#     document_chain = create_stuff_documents_chain(llm, rag_prompt)
#     return create_retrieval_chain(vector_store.as_retriever(), document_chain)






# import os
# from langchain_community.document_loaders import PyPDFLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_community.embeddings import HuggingFaceEmbeddings
# from langchain_community.vectorstores import Chroma
# from langchain_openai import ChatOpenAI
# from langchain.prompts import PromptTemplate
# from langchain.chains.combine_documents import create_stuff_documents_chain
# from langchain.chains import create_retrieval_chain

# # -----------------------------
# # Vector store
# # -----------------------------
# def get_or_create_vector_store(file_path: str, collection_name: str) -> Chroma:
#     persist_directory = f"./chroma_db/{collection_name}"

#     if os.path.exists(persist_directory):
#         print(f"Loading existing vector store for '{collection_name}'...")
#         embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
#         return Chroma(persist_directory=persist_directory, embedding_function=embedding_model)

#     print(f"Creating new vector store for '{collection_name}'...")
#     loader = PyPDFLoader(file_path)
#     documents = loader.load()

#     # text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
#     text_splitter = RecursiveCharacterTextSplitter(
#     chunk_size=500,    # smaller chunks
#     chunk_overlap=50
# )


#     docs = text_splitter.split_documents(documents)

#     embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
#     vector_store = Chroma.from_documents(docs, embedding_model, persist_directory=persist_directory)

#     print(f"Vector store created for '{collection_name}'!")
#     return vector_store

# # -----------------------------
# # RAG chain with OpenRouter Kimi
# # -----------------------------
# def get_rag_chain(vector_store: Chroma):
#     llm = ChatOpenAI(
#         model="moonshotai/kimi-k2",
#         temperature=0.7,
#         openai_api_key=os.getenv("OPENAI_API_KEY"),   # must not be None
#         openai_api_base=os.getenv("OPENAI_API_BASE", "https://openrouter.ai/api/v1")
#     )

#     rag_prompt = PromptTemplate.from_template("""
#         You are an AI assistant for a personalized knowledge base.
#         Use the following retrieved context to answer the question.
#         If you cannot find the answer in the provided context, politely state that you do not have enough information to answer.

#         Context:
#         {context}

#         Question:
#         {input}
#     """)

#     document_chain = create_stuff_documents_chain(llm, rag_prompt)
#     return create_retrieval_chain(vector_store.as_retriever(), document_chain)




















import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain

# -----------------------------
# Vector store with smaller chunks
# -----------------------------
def get_or_create_vector_store(file_path: str, collection_name: str) -> Chroma:
    persist_directory = f"./chroma_db/{collection_name}"

    if os.path.exists(persist_directory):
        print(f"Loading existing vector store for '{collection_name}'...")
        embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        return Chroma(
            persist_directory=persist_directory,
            embedding_function=embedding_model
        )

    print(f"Creating new vector store for '{collection_name}'...")

    # Load PDF
    loader = PyPDFLoader(file_path)
    documents = loader.load()

    # Split into smaller chunks to reduce tokens
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,     # smaller chunks
        chunk_overlap=50
    )
    docs = text_splitter.split_documents(documents)

    # Create embeddings and store in ChromaDB
    embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vector_store = Chroma.from_documents(
        docs,
        embedding_model,
        persist_directory=persist_directory
    )

    print(f"Vector store created for '{collection_name}'!")
    return vector_store

# -----------------------------
# RAG chain with token limits
# -----------------------------
def get_rag_chain(vector_store: Chroma):
    # Limit max tokens to avoid 402 errors
    llm = ChatOpenAI(
        model="moonshotai/kimi-k2",
        temperature=0.7,
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        openai_api_base=os.getenv("OPENAI_API_BASE", "https://openrouter.ai/api/v1"),
        max_tokens=2000   # limit response tokens
    )

    # Retrieve top-k chunks only
    retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 5})

    # Custom prompt
    rag_prompt = PromptTemplate.from_template("""
        You are an AI assistant for a personalized knowledge base.
        Use the following retrieved context to answer the question.
        If you cannot find the answer in the provided context, politely state that you do not have enough information to answer.

        Context:
        {context}

        Question:
        {input}
    """)

    document_chain = create_stuff_documents_chain(llm, rag_prompt)
    return create_retrieval_chain(retriever, document_chain)


