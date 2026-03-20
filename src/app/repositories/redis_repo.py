import json

import redis
from pydantic import TypeAdapter

from src.app.schemas.tasks import TaskResponse

redis_server = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

task_list_adapter = TypeAdapter(list[TaskResponse])

def add_tasks(tasks, username, status, limit, offset):
    cache_key = f"tasks:list:{username}:{status}:{limit}:{offset}"
    json_tasks = task_list_adapter.dump_json(tasks).decode('utf-8')
    redis_server.hset(f'{cache_key}', mapping={'tasks': json_tasks})
    return get_tasks(username, status, limit, offset)

def get_tasks(username, status, limit, offset):
    cache_key = f"tasks:list:{username}:{status}:{limit}:{offset}"
    response_tasks = redis_server.hget(f'{cache_key}', 'tasks')
    if response_tasks is None:
        return None
    return task_list_adapter.validate_json(response_tasks)

def delete_cash(username):
    redis_server.hdel(f'tasks:{username}', 'tasks')
    return None