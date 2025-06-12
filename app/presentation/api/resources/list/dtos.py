import datetime as dt
from uuid import UUID

from pydantic import BaseModel


# Base
class TaskListBasePayload(BaseModel):

    name: str


class TaskListBaseResponse(TaskListBasePayload):

    uuid: UUID
    created_at: dt.datetime
    updated_at: dt.datetime


# Get
class TaskListGetResponse(TaskListBaseResponse):
    pass


# Create
class TaskListCreatePayload(TaskListBasePayload):
    pass


class TaskListCreateResponse(TaskListBaseResponse):
    pass


# Update
class TaskListUpdatePayload(TaskListBasePayload):
    pass


class TaskListUpdateResponse(TaskListBaseResponse):
    pass


# Delete
class TaskListDeleteResponse(BaseModel):
    msg: str
