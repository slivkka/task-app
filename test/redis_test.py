import json
import time

import redis
from pydantic import TypeAdapter

from src.app.db.models.tasks import Task
from src.app.schemas.tasks import TaskResponse

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

task_list_adapter = TypeAdapter(list[TaskResponse])

def add_tasks(tasks, username):
    json_tasks = task_list_adapter.dump_json(tasks).decode('utf-8')
    r.hset(f'tasks:{username}', mapping={'tasks': json_tasks})
    return get_tasks(username)

def get_tasks(username):
    response_tasks = r.hget(f'tasks:{username}', 'tasks')
    return task_list_adapter.validate_json(response_tasks)


