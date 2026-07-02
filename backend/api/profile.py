from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.database import SessionLocal
from models.research import Research
from models.user import User

from auth.dependencies import get_current_user

router = APIRouter(
    prefix="/profile",
    tags=["Profile"]
)


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
# Research History
# ----------------------------

@router.get("/history")
def get_history(

    current_user: User = Depends(get_current_user),

    db: Session = Depends(get_db)

):

    history = (

        db.query(Research)

        .filter(
            Research.username == current_user.username
        )

        .all()

    )

    return history