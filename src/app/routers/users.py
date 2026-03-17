from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm


from src.app.schemas.auth import TokenResponse, RefreshRequest, TokenRequest
from src.app.schemas.users import CreateUser
from src.app.services.auth import Authentification

from src.app.services.users import create_user

router = APIRouter(tags=["users"])

@router.post("/auth/register")
async def create_user_(user: CreateUser):
    return await create_user(user)

@router.post("/auth/login", response_model=TokenResponse)
async def user_login_(data: OAuth2PasswordRequestForm = Depends()):
    return await Authentification.login(username=data.username,password=data.password)

@router.post("/auth/me")
async def check_refresh(token: TokenRequest):
    return await Authentification.check_access_token(token.token)

@router.post("/auth/refresh")
async def check_refresh(token: RefreshRequest):
    return await Authentification.check_refresh_token(token.refresh_token)

@router.post("/auth/logout")
async def check_refresh(token: RefreshRequest):
    return await Authentification.logout(token.refresh_token)