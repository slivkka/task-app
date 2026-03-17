from pydantic import BaseModel, Field


class CreateTask(BaseModel):
    title: str
    description: str

class TaskCreatedOrExists(BaseModel):
    message: str

class CompleteTask(BaseModel):
    id: int

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    status: str

class GetTask(BaseModel):
    status: str = None
    limit: int = Field(5, gt=0, le=10)
    offset: int = Field(0, ge = 0)

class DeleteTaskResponse(BaseModel):
    message: str
