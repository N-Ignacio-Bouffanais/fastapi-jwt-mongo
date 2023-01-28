from fastapi import APIRouter, Response, status
from ..models.user import UserLoginSchema
from starlette.status import HTTP_204_NO_CONTENT
from ..config.db import conn
from app.auth.jwt_handler import signJWT

users_router = APIRouter()

@users_router.get("/users", tags=["users"])
def get_users(request):
    print("users")
    