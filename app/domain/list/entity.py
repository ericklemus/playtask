import datetime as dt
from uuid import UUID

from pydantic import BaseModel


class TaskList(BaseModel):
    name: str


class TaskListCreate(TaskList):
    uuid: UUID
    created_at: dt.datetime
    updated_at: dt.datetime
