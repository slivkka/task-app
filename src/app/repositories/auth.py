from src.app.db.models.refresh_token import RefreshToken


async def create_refresh_token(user, token, expires_at, is_revoked):
    refresh_token = await RefreshToken.create(
        user = user,
        token = token,
        expires_at = expires_at,
        is_revoked = is_revoked
    )
    return refresh_token

async def get_token(refresh_token: str) -> RefreshToken:
    token = await RefreshToken.get(token=refresh_token)
    return token

async def find_rf_by_username(username):
    return await RefreshToken.get_or_none(user=username)


async def revoke(rf: RefreshToken):
    rf.is_revoked = True
    await rf.save()