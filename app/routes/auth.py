from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import UserCreate, UserResponse, TokenResponse
from app.services.auth_service import create_user, authenticate_user

router = APIRouter()


@router.post("/signup/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def signup(user_data: UserCreate, db: Session = Depends(get_db)):
    """Registers a new user."""
    user = create_user(db, user_data)
    if not user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user


@router.post("/login/", response_model=TokenResponse)
def login(user_data: UserCreate, db: Session = Depends(get_db)):
    """Logs in the user and returns a JWT token."""
    token = authenticate_user(db, user_data.email, user_data.password)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"access_token": token, "token_type": "bearer"}
