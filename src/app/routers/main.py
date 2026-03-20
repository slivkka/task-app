from typing import Annotated

from fastapi import APIRouter, Query, Depends

from src.app.auth.security import get_current_user
from src.app.db.models.users import User
from src.app.schemas.tasks import TaskResponse, GetTask, TaskCreatedOrExists
from src.app.services.main import create_task, list_tasks, complete_task, \
    delete_task, CreateTask, get_task

router = APIRouter(tags=["tasks"])

@router.post("/tasks", response_model=TaskCreatedOrExists)
async def create_task_(task: CreateTask,
                       current_user: User = Depends(get_current_user)):
    return await create_task(task, current_user)

@router.get("/tasks/{task_id}", response_model=TaskResponse)
async def get_task_(task_id: int):
    return await get_task(task_id)

@router.get("/tasks", response_model=list[TaskResponse])
async def list_tasks_(
        filter_query: Annotated[GetTask, Query()],
        current_user: User = Depends(get_current_user)
):
    return await list_tasks(filter_query, current_user)

@router.patch("/tasks/{task_id}", response_model=TaskResponse)
async def complete_task_(task_id: int):
    return await complete_task(task_id)

@router.delete("/tasks/{task_id}")
async def delete_task_(task_id: int,
                       current_user: User = Depends(get_current_user)):
    return await delete_task(task_id, current_user)

