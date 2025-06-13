import datetime as dt
from uuid import UUID

from pydantic import BaseModel


# Base
class TaskBasePayload(BaseModel):

    name: str
    completed: bool
    priority: str


class TaskBaseResponse(TaskBasePayload):

    uuid: UUID
    created_at: dt.datetime
    updated_at: dt.datetime


class TaskAllBaseResponse(BaseModel):

    name: str
    completed: bool
    priority: str
    uuid: UUID
    created_at: dt.datetime
    updated_at: dt.datetime

    class Config:
        from_attributes = True


# Get
class TaskAllResponse(BaseModel):
    tasks: list[TaskAllBaseResponse]
    completed_percentage: float


class TaskGetResponse(TaskBaseResponse):
    pass


# Create
class TaskCreatePayload(TaskBasePayload):
    pass


class TaskCreateResponse(TaskBaseResponse):
    pass


# Update
class TaskUpdatePayload(TaskBasePayload):
    pass


class TaskUpdateResponse(TaskBaseResponse):
    pass


# Delete
class TaskDeleteResponse(BaseModel):
    msg: str
