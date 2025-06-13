import datetime as dt
from uuid import UUID

from pydantic import BaseModel


class TaskListCreate(BaseModel):
    name: str


class TaskList(TaskListCreate):
    uuid: UUID
    created_at: dt.datetime
    updated_at: dt.datetime
