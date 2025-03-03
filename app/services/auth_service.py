from sqlalchemy.orm import Session
from app.models import User
from app.schemas import UserCreate
from app.utils.security import hash_password, verify_password, create_access_token


def create_user(db: Session, user_data: UserCreate):
    """Creates a new user with hashed password."""
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    if existing_user:
        return None  # User already exists

    hashed_pw = hash_password(user_data.password)
    new_user = User(email=user_data.email, hashed_password=hashed_pw)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def authenticate_user(db: Session, email: str, password: str):
    """Authenticates user and returns JWT token if successful."""
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(password, user.hashed_password):
        return None
    return create_access_token({"sub": user.email})
