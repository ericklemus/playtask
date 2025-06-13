from abc import ABC, abstractmethod
from uuid import UUID

from app.infrastructure.database.models.base import TaskList as TaskListModel


class TaskList(ABC):

    @abstractmethod
    async def all(self, filters: dict) -> list[TaskListModel]:
        pass

    @abstractmethod
    async def get(self, uuid: UUID) -> TaskListModel:
        pass

    @abstractmethod
    async def create(self, task_data: dict) -> TaskListModel:
        pass

    @abstractmethod
    async def update(self, uuid: UUID, task_data: dict) -> TaskListModel:
        pass

    @abstractmethod
    async def delete(self, uuid: UUID) -> None:
        pass
