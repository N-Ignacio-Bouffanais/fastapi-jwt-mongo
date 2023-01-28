from fastapi import FastAPI
from app.routers.task import tasks_router
from app.routers.user import users_router

app = FastAPI(
    title="FastAPI & Mongo CRUD",
    description="this is a REST API using fastapi, mongodb and JWT for authentication",
    version="0.0.1",
)

app.include_router(users_router)
app.include_router(tasks_router)