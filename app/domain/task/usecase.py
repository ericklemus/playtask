from abc import ABC, abstractmethod
from uuid import UUID

from app.domain.task.entity import Task as TaskEntity


class TaskAll(ABC):

    @abstractmethod
    async def execute(self) -> TaskEntity:
        pass


class TaskGet(ABC):

    @abstractmethod
    async def execute(self, uuid: UUID) -> TaskEntity:
        pass


class TaskCreate(ABC):

    @abstractmethod
    async def execute(self, entity: TaskEntity) -> TaskEntity:
        pass


class TaskUpdate(ABC):

    @abstractmethod
    async def execute(self, uuid: UUID, entity: TaskEntity) -> TaskEntity:
        pass


class TaskDelete(ABC):

    @abstractmethod
    async def execute(self, uuid: UUID) -> None:
        pass
