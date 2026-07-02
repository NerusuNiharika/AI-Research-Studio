import os

from dotenv import load_dotenv

load_dotenv()


# API Keys

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")


# LLM

MODEL_NAME = "llama-3.1-8b-instant"

TEMPERATURE = 0


# Qdrant

QDRANT_URL = "http://localhost:6333"

COLLECTION_NAME = "research_documents"



# Embeddings

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"


# Text Splitter

CHUNK_SIZE = 500

CHUNK_OVERLAP = 100


# Directories

DOCS_FOLDER = "docs"

UPLOAD_FOLDER = "uploads"

REPORT_FOLDER = "reports"

PRESENTATION_FOLDER = "presentations"

SECRET_KEY = "your_super_secret_key_change_this"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60