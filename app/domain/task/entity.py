import datetime as dt
from enum import Enum
from uuid import UUID
from typing import Optional

from pydantic import BaseModel


class Priority(str, Enum):
    lowest = "lowest"
    low = "low"
    medium = "medium"
    high = "high"
    highest = "highest"


class TaskFilter(BaseModel):
    tasklist_id: UUID
    priority: Optional[Priority]
    completed: Optional[bool]


class TaskCreate(BaseModel):
    name: str
    status: bool
    priority: Priority


class Task(TaskCreate):
    uuid: UUID
    created_at: dt.datetime
