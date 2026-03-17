from fastapi import HTTPException

from src.app.db.models.users import User
from src.app.repositories.tasks import (
    create_task as repo_create_task,
    list_tasks as repo_list_tasks,
    complete_task as repo_complete_task,
    get_task_by_id,
    delete_task as repo_delete_task,
)
from src.app.schemas.tasks import CreateTask, GetTask


async def create_task(task: CreateTask, current_user: User):
    task = await repo_create_task(task, current_user)
    return task

async def list_tasks(task: GetTask, user: User):
    tasks = await repo_list_tasks(task, user)
    return tasks

async def get_task(task_id:int):
    task = await get_task_by_id(task_id=task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

async def complete_task(task_id: int):
    task = await get_task_by_id(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    await repo_complete_task(task)
    return task

async def delete_task(task_id: int):
    task = await get_task_by_id(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    await repo_delete_task(task)
    return {"detail": "Task was successfully deleted"}