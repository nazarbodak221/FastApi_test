from pydantic import BaseModel, EmailStr, constr

from app.models import User


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True


class TokenResponse(BaseModel):
    access_token: str
    token_type: str


class ArticleCreate(BaseModel):
    text: constr(max_length=1048576)  # Limit the text size to 1MB

    class Config:
        str_min_length = 1
        str_strip_whitespace = True
        str_max_length = 1048576


class ArticleResponse(BaseModel):
    user_email: EmailStr
    text: str

    class Config:
        orm_mode = True


class PostResponse(BaseModel):
    post_id: int
    text: str


class PostDeleteResponse(BaseModel):
    success: bool
    message: str
