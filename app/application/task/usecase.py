from uuid import UUID

from app.domain.task.exception import TaskNotFoundError
from app.domain.task.entity import Task as TaskEntity
from app.domain.task.entity import TaskCreate as TaskCreateEntity
from app.domain.task.entity import TaskFilter as TaskFilterEntity
from app.domain.task.repository import Task as TaskRepository
from app.domain.task.usecase import (
    TaskAll as TaskAllUsecase,
    TaskGet as TaskGetUsecase,
    TaskCreate as TaskCreateUsecase,
    TaskUpdate as TaskUpdateUsecase,
    TaskDelete as TaskDeleteUsecase,
)


class TaskAll(TaskAllUsecase):

    def __init__(self, repository: TaskRepository) -> None:
        self.repository = repository

    async def execute(self, entity: TaskFilterEntity) -> TaskEntity:
        self.repository.all(entity.model_dump(exclude_none=True))


class TaskGet(TaskGetUsecase):

    def __init__(self, repository: TaskRepository):
        self.repository = repository

    async def execute(self, tasklist_id: UUID, task_id: UUID) -> TaskEntity:
        instance_dict = await self.repository.get(tasklist_id, task_id)
        if not instance_dict:
            raise TaskNotFoundError
        return TaskEntity(**instance_dict)


class TaskCreate(TaskCreateUsecase):

    def __init__(self, repository: TaskRepository) -> None:
        self.repository = repository

    async def execute(self, tasklist_id: UUID, entity: TaskCreateEntity):
        instance_dict = await self.repository.create(
            tasklist_id, entity.model_dump(exclude_defaults=True)
        )
        if not instance_dict:
            raise TaskNotFoundError
        return TaskEntity(**instance_dict)


class TaskUpdate(TaskUpdateUsecase):

    def __init__(self, repository: TaskRepository) -> None:
        self.repository = repository

    async def execute(self, tasklist_id: UUID, task_id: UUID, entity: TaskCreateEntity):
        instance_dict = await self.repository.update(
            tasklist_id, task_id, entity.model_dump(exclude_defaults=True)
        )
        if not instance_dict:
            raise TaskNotFoundError
        return TaskEntity(**instance_dict)


class TaskDelete(TaskDeleteUsecase):

    def __init__(self, repository: TaskRepository) -> None:
        self.repository = repository

    async def execute(self, tasklist_id: UUID, task_id: UUID):
        return await self.repository.delete(tasklist_id, task_id)
