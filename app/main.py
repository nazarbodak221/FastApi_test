from fastapi import FastAPI, Depends

from app.dependencies.auth import get_current_user
from app.models import User
from .routes.auth import router as auth_router
from .routes.posts import router as post_router

app = FastAPI()

# Register auth routes
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(post_router)


@app.get('/user_info/')
def protected_route(user: User = Depends(get_current_user)):
    return {"message": "Welcome!", "user": user.email}
