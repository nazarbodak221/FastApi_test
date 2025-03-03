# services/post_service.py
from typing import List
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Article, User
from app.schemas import PostDeleteResponse
from fastapi import HTTPException, status, Depends


class PostService:
    def __init__(self, db: Session):
        self.db = db

    def create_post(self, text: str, user: User) -> Article:
        """Create a new post."""
        post = Article(text=text, user_id=user.id)
        self.db.add(post)
        self.db.commit()
        self.db.refresh(post)
        return post

    def get_user_posts(self, user: User):
        """Retrieve all posts by a user."""
        posts = self.db.query(Article).filter(Article.user_id == user.id).all()
        return {user.email: [post.text for post in posts]}

    def delete_post(self, post_id: int, user: User) -> PostDeleteResponse:
        """Delete a post."""
        post = self.db.query(Article).filter(Article.id == post_id, Article.user_id == user.id).first()
        if post is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

        self.db.delete(post)
        self.db.commit()
        return PostDeleteResponse(success=True, message="Post deleted successfully")


# Create instance of the PostService
def get_post_service(db: Session = Depends(get_db)):
    return PostService(db)
