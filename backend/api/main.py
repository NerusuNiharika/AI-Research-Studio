from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from api.routes import router

# Database imports
from database.database import engine, Base
import models.user
import models.research

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Research Studio API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API routes
app.include_router(router)

# Serve generated files
app.mount("/reports", StaticFiles(directory="reports"), name="reports")
app.mount("/presentations", StaticFiles(directory="presentations"), name="presentations")


@app.get("/")
def home():
    return {
        "message": "AI Research Studio Backend Running"
    }