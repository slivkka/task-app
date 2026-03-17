from fastapi import Depends
from jose import jwt, JWTError, ExpiredSignatureError
from datetime import datetime, timedelta

from src.app.auth.o2auth_scheme import oauth2_scheme

from src.app.repositories.users import get_user_by_username
from src.core.config.settings import settings

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM

def create_token(user_id, username):

    payload = {
        "user_id": user_id,
        "username": username,
        "exp": datetime.utcnow() + timedelta(minutes=1),
        "type": "access"
    }

    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def create_refresh_token(user_id, username):

    payload = {
        "user_id": user_id,
        "username": username,
        "exp": datetime.utcnow() + timedelta(minutes=10080),
        "type": "refresh"
    }

    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def decode_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except ExpiredSignatureError:
        return {"msg": 'Token is expired'}
    except JWTError:
        return {"msg": 'Signature is invalid'}


async def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = decode_token(token)
    return await get_user_by_username(payload["username"])


def verify_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload["user_id"]
    except:
        return None

