from uuid import UUID, uuid4
from pydantic import BaseModel, PositiveFloat, Field
from typing import Optional


class Task(BaseModel):
    uuid: UUID
    name: str

class TaskCreate(BaseModel):
    name: str