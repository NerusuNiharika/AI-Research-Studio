import os
import shutil

from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Form,
    Depends,
)

from sqlalchemy.orm import Session

from workflows.graph import graph

from models.response import ResearchResponse
from models.research import Research
from models.user import User

from rag.upload_pdf import upload_pdf_to_qdrant

from config.settings import UPLOAD_FOLDER

from database.database import SessionLocal

from auth.dependencies import get_current_user


router = APIRouter()


# ----------------------------
# Database Dependency
# ----------------------------

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# ----------------------------
# Research API
# ----------------------------

@router.post(
    "/research",
    response_model=ResearchResponse
)
async def research(

    topic: str = Form(...),

    file: UploadFile | None = File(None),

    current_user: User = Depends(get_current_user),

    db: Session = Depends(get_db)

):

    # ----------------------------------
    # Save Uploaded PDF
    # ----------------------------------

    if file is not None:

        os.makedirs(
            UPLOAD_FOLDER,
            exist_ok=True
        )

        pdf_path = os.path.join(
            UPLOAD_FOLDER,
            file.filename
        )

        with open(pdf_path, "wb") as buffer:

            shutil.copyfileobj(
                file.file,
                buffer
            )

        print(f"Uploaded PDF: {file.filename}")

        upload_pdf_to_qdrant(pdf_path)

    # ----------------------------------
    # Initial LangGraph State
    # ----------------------------------

    initial_state = {

        "topic": topic,

        "research_plan": [],

        "research_results": [],

        "reviewer_feedback": "",

        "approved": False,

        "retry_count": 0,

        "report": "",

        "report_path": "",

        "ppt_path": ""

    }

    # ----------------------------------
    # Execute Workflow
    # ----------------------------------

    result = graph.invoke(initial_state)

    # ----------------------------------
    # Save Research History
    # ----------------------------------

    history = Research(

        username=current_user.username,

        topic=topic,

        report_path=result["report_path"],

        ppt_path=result["ppt_path"]

    )

    db.add(history)

    db.commit()

    db.refresh(history)

    print("Research History Saved")

    # ----------------------------------
    # Response
    # ----------------------------------

    return ResearchResponse(

        report=result["report"],

        report_path=result["report_path"],

        ppt_path=result["ppt_path"]

    )