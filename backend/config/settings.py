import os

from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")

QDRANT_URL = os.getenv("QDRANT_URL")

QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")

COLLECTION_NAME = os.getenv("COLLECTION_NAME")

SECRET_KEY = os.getenv("SECRET_KEY")
# LLM

MODEL_NAME = "llama-3.1-8b-instant"

TEMPERATURE = 0


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

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60