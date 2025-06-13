from uuid import UUID

from app.domain.list.exception import TaskListNotFoundError
from app.domain.list.entity import TaskList as TaskListEntity
from app.domain.list.entity import TaskListCreate as TaskListCreateEntity
from app.domain.list.repository import TaskList as TaskListRepository
from app.domain.list.usecase import (
    TaskListAll as TaskListAllUsecase,
    TaskListGet as TaskListGetUsecase,
    TaskListCreate as TaskListCreateUsecase,
    TaskListUpdate as TaskListUpdateUsecase,
    TaskListDelete as TaskListDeleteUsecase,
)


class TaskListAll(TaskListAllUsecase):

    def __init__(self, repository: TaskListRepository) -> None:
        self.repository = repository

    async def execute(self) -> TaskListEntity:
        self.repository.all()


class TaskListGet(TaskListGetUsecase):

    def __init__(self, repository: TaskListRepository):
        self.repository = repository

    async def execute(self, tasklist_id: UUID) -> TaskListEntity:
        instance_dict = await self.repository.get(tasklist_id)
        if not instance_dict:
            raise TaskListNotFoundError
        return TaskListEntity(**instance_dict)


class TaskListCreate(TaskListCreateUsecase):

    def __init__(self, repository: TaskListRepository) -> None:
        self.repository = repository

    async def execute(self, entity: TaskListCreateEntity):
        instance_dict = await self.repository.create(
            entity.model_dump(exclude_defaults=True)
        )
        if not instance_dict:
            raise TaskListNotFoundError
        return TaskListEntity(**instance_dict)


class TaskListUpdate(TaskListUpdateUsecase):

    def __init__(self, repository: TaskListRepository) -> None:
        self.repository = repository

    async def execute(self, tasklist_id: UUID, entity: TaskListCreateEntity):
        instance_dict = await self.repository.update(
            tasklist_id, entity.model_dump(exclude_defaults=True)
        )
        if not instance_dict:
            raise TaskListNotFoundError
        return TaskListEntity(**instance_dict)


class TaskListDelete(TaskListDeleteUsecase):

    def __init__(self, repository: TaskListRepository) -> None:
        self.repository = repository

    async def execute(self, tasklist_id: UUID):
        return await self.repository.delete(tasklist_id)
