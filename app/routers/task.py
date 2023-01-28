from fastapi import APIRouter, Response, status
from ..models.task import Task
from ..schemas.task import TaskEntity
from starlette.status import HTTP_204_NO_CONTENT
from ..config.db import conn

tasks_router = APIRouter()


@tasks_router.get("/tasks", tags=["tasks"])

def get_tasks():
    return TaskEntity(conn.local.task.find())