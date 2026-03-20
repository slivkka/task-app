from fastapi import HTTPException

from src.app.db.models.users import User
from src.app.repositories.tasks import (
    create_task as repo_create_task,
    list_tasks as repo_list_tasks,
    complete_task as repo_complete_task,
    get_task_by_id,
    delete_task as repo_delete_task,
)
from src.app.schemas.tasks import CreateTask, GetTask, TaskResponse

from src.app.repositories.redis_repo import add_tasks as redis_add
from src.app.repositories.redis_repo import get_tasks as redis_get
from src.app.repositories.redis_repo import delete_cash as redis_delete


async def create_task(task: CreateTask, current_user: User):
    task = await repo_create_task(task, current_user)
    redis_delete(current_user.username)
    return task

async def list_tasks(query: GetTask, user: User):

    username = user.username
    tasks_from_redis = redis_get(username,
                         query.status, query.limit, query.offset)
    if tasks_from_redis:
        return tasks_from_redis
    else:
        tasks = await repo_list_tasks(query, user)
        return redis_add(tasks, username,
                         query.status, query.limit, query.offset)

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

async def delete_task(task_id: int, current_user: User):
    task = await get_task_by_id(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    await repo_delete_task(task)
    redis_delete(current_user.username)
    return {"detail": "Task was successfully deleted"}