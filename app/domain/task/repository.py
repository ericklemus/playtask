from abc import ABC, abstractmethod
from uuid import UUID

from app.models import Task as TaskModel


class Task(ABC):

    @abstractmethod
    async def all(self, filters: dict) -> list[TaskModel]:
        pass

    @abstractmethod
    async def get(self, uuid: UUID) -> TaskModel:
        pass

    @abstractmethod
    async def create(self, task_data: dict) -> TaskModel:
        pass

    @abstractmethod
    async def update(self, uuid: UUID, task_data: dict) -> TaskModel:
        pass

    @abstractmethod
    async def delete(self, uuid: UUID) -> None:
        pass
