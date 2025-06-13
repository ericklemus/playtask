from abc import ABC, abstractmethod
from uuid import UUID

from app.infrastructure.database.models.base import Task as TaskModel


class Task(ABC):

    @abstractmethod
    async def all(self, filters: dict) -> list[TaskModel]:
        pass

    @abstractmethod
    async def get(self, tasklist_id: UUID, task_id: UUID) -> TaskModel:
        pass

    @abstractmethod
    async def create(self, tasklist_id: UUID, data: dict) -> TaskModel:
        pass

    @abstractmethod
    async def update(self, tasklist_id: UUID, task_id: UUID, data: dict) -> TaskModel:
        pass

    @abstractmethod
    async def delete(self, tasklist_id: UUID, task_id: UUID) -> None:
        pass
