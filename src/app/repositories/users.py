from argon2 import PasswordHasher

from src.app.db.models.users import User
from src.app.schemas.users import CreateUser, LoginUser

ph = PasswordHasher()

async def create_user(user: CreateUser):
    user = await User.get_or_create(
        username = user.username,
        hashed_password = ph.hash(user.hashed_password),
        email = user.email
   )
    return user

async def get_user(user: LoginUser):
    user = await User.get_or_none(username = user.username)
    if not user:
        return None
    return user

async def get_user_by_username(username):
    user = await User.get_or_none(username=username)
    return user

async def get_all_users():
    return await User.all()