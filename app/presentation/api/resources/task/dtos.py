import datetime as dt
from uuid import UUID

from pydantic import BaseModel


# Base
class TaskBasePayload(BaseModel):

    name: str
    completed: bool
    priority: str
    tasklist_id: UUID


class TaskBaseResponse(TaskBasePayload):

    uuid: UUID
    created_at: dt.datetime
    updated_at: dt.datetime


# Get
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