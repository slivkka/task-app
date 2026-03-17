import datetime

from pydantic import BaseModel


class CreateRefreshToken(BaseModel):
    user: str
    token: str
    expires_at: datetime.datetime
    is_revoked: bool

class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str

class RefreshRequest(BaseModel):
    refresh_token: str

class TokenRequest(BaseModel):
    token: str
