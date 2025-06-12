from uuid import UUID
from pydantic import BaseModel


class Task(BaseModel):
    uuid: UUID
    name: str


class TaskCreate(BaseModel):
    name: str
