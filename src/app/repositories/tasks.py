from src.app.db.models.tasks import Task
from src.app.db.models.users import User
from src.app.schemas.tasks import GetTask, CreateTask


async def create_task(task:CreateTask, current_user: User):
    new_task = await Task.get_or_create(title=task.title,
                                         description=task.description,
                                        user=current_user)
    if not new_task[1]:
        return {"message": "task already exists"}
    else:
        return {"message": "task was successfully created"}

async def list_tasks(task: GetTask, user: User):
    if task.status is None:
        return await (Task.all().order_by("id").
                      limit(task.limit).offset(task.offset).filter(user=user))
    else:
        return await (Task.all().filter(status=task.status, user=user).
                      order_by("id").limit(task.limit).offset(task.offset))

async def get_task_by_id(task_id: int) -> Task | None:
    task = await Task.get_or_none(id=task_id)
    return task

async def complete_task(task: Task) -> Task:
    task.status = 'completed'
    await task.save()
    return task

async def delete_task(task: Task) -> None:
    await task.delete()