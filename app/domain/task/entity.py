import datetime as dt
from enum import Enum
from uuid import UUID

from pydantic import BaseModel


class Priority(str, Enum):
    lowest = "lowest"
    low = "low"
    medium = "medium"
    high = "high"
    highest = "highest"


class Task(BaseModel):
    name: str
    status: bool
    priority: Priority


class TaskCreate(Task):
    uuid: UUID
    created_at: dt.datetime
