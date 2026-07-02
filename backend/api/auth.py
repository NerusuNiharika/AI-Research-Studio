from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from models.auth import (
    RegisterRequest,
    LoginRequest,
    TokenResponse,
)

from auth.security import (
    hash_password,
    verify_password,
)

from auth.jwt_handler import create_access_token
from database.database import SessionLocal
from models.user import User
from models.auth import RegisterRequest
from auth.security import hash_password

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


# Database Dependency
def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# -------------------------
# Register API
# -------------------------

@router.post("/register")
def register(
    user: RegisterRequest,
    db: Session = Depends(get_db)
):

    # Check username
    existing_user = db.query(User).filter(
        User.username == user.username
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Username already exists."
        )

    # Check email
    existing_email = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_email:
        raise HTTPException(
            status_code=400,
            detail="Email already registered."
        )

    # Create new user
    new_user = User(
        username=user.username,
        email=user.email,
        password=hash_password(user.password)
    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    return {
        "message": "Registration Successful"
    }
@router.post(
    "/login",
    response_model=TokenResponse
)
def login(
    user: LoginRequest,
    db: Session = Depends(get_db)
):

    # Find user
    db_user = db.query(User).filter(
        User.username == user.username
    ).first()

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password."
        )

    # Verify password
    if not verify_password(
        user.password,
        db_user.password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password."
        )

    # Create JWT
    access_token = create_access_token(
        {
            "sub": db_user.username
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }