from fastapi import APIRouter, Response, status

users_router = APIRouter()

@users_router.get("/users", tags=["users"])
def get_users(request):
    print("users")
    