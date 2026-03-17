from fastapi import FastAPI
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise

from src.app.routers.main import router as tasks_router
from src.app.routers.users import router as users_router

from src.core.config.settings import TORTOISE_ORM

app = FastAPI()

routers = [tasks_router, users_router]

for router in routers:
    app.include_router(router)


register_tortoise(
    app,
    config=TORTOISE_ORM
)

print(Tortoise.apps)