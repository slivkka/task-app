from pydantic import BaseModel, EmailStr


class CreateUser(BaseModel):
    username: str
    email: EmailStr
    hashed_password: str

class LoginUser(BaseModel):
    username: str
    password: str