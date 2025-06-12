import datetime as dt
from enum import Enum
from uuid import UUID

from pydantic import BaseModel, Field

class Priority(str, Enum):
    lowest = "lowest"
    low = "low"
    medium = "medium"
    high = "high"
    highest = "highest"

class Task(BaseModel):
    uuid: UUID
    name: str
    status: bool
    priority: Priority
