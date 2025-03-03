# routes/post.py
from typing import List

from fastapi import APIRouter, Depends
from app.schemas import ArticleCreate, PostDeleteResponse, PostResponse
from app.services.post_service import PostService, get_post_service
from app.dependencies.auth import get_current_user
from app.models import User
from app.cache.article_cache import cache_response

router = APIRouter()


@router.post("/posts/", response_model=PostResponse)
async def add_post(
    article: ArticleCreate,
    user: User = Depends(get_current_user),
    post_service: PostService = Depends(get_post_service)
):
    """Add a new post"""
    post = post_service.create_post(text=article.text, user=user)
    return PostResponse(post_id=post.id, text=post.text)


@router.get("/posts/")
@cache_response(ttl=300)
async def get_posts(user: User = Depends(get_current_user), post_service: PostService = Depends(get_post_service)):
    """Get all posts of a user"""
    posts = post_service.get_user_posts(user=user)
    return posts


@router.delete("/posts/{post_id}/", response_model=PostDeleteResponse)
async def delete_post(
    post_id: int,
    user: User = Depends(get_current_user),
    post_service: PostService = Depends(get_post_service)
):
    """Delete a post by postID"""
    result = post_service.delete_post(post_id=post_id, user=user)
    return result
