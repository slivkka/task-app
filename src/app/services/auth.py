from argon2.exceptions import VerifyMismatchError
from fastapi import HTTPException

from src.app.repositories.auth import get_token, find_rf_by_username, revoke
from src.app.repositories.auth import create_refresh_token as repo_create_fr
from src.app.auth.security import create_refresh_token as sec_create_rf, \
    decode_token, create_token
from src.app.repositories.users import get_user_by_username
from src.app.services.users import ph

class Authentification:
    @classmethod
    async def check_access_token(cls, token):
        decode_token(token)
        return {"message": "access granted"}

    @classmethod
    async def check_refresh_token(cls, refresh_token):
        token = await get_token(refresh_token)
        is_revoke = token.is_revoked
        payload = decode_token(refresh_token)
        if not is_revoke:
            token = create_token(payload["user_id"], payload["username"])
            return {"access_token": token,
                    "token_type": "bearer"}
        else:
            raise HTTPException

    @classmethod
    async def create_refresh_token(cls, username, user_id):
        rf_token = sec_create_rf(user_id=user_id, username=username)
        payload_rf_token = decode_token(rf_token)
        await repo_create_fr(user = username,
                             token = rf_token,
                             expires_at = payload_rf_token["exp"],
                             is_revoked = False )

        return rf_token

    @classmethod
    async def login(cls, username, password):
        user = await get_user_by_username(username=username)
        if user:
            try:
                ph.verify(user.hashed_password, password)
            except VerifyMismatchError:
                return None
        elif user is None:
            raise HTTPException(status_code=401, detail="Wrong user")

        rf = await find_rf_by_username(username=username)
        if rf:
            await rf.delete()
        elif rf is None:
            pass

        token = create_token(user.id, user.username)
        refresh_token = await Authentification.create_refresh_token(user_id=user.id,
                                             username=user.username)
        return {"access_token": token,
                "refresh_token": refresh_token,
                "token_type": "bearer"}

    @classmethod
    async def logout(cls, token):
        payload = decode_token(token)
        username = payload["username"]
        rf = await find_rf_by_username(username=username)
        if not rf.is_revoked:
            await revoke(rf)
        elif rf is None:
            raise HTTPException

        return {"message": "successfully logged out"}
