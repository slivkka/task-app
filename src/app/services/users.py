from argon2 import PasswordHasher

from src.app.schemas.users import CreateUser

from src.app.repositories.users import create_user as repo_create_user

ph = PasswordHasher()


async def create_user(user: CreateUser):

    return await repo_create_user(user)


