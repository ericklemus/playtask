from abc import ABC, abstractmethod
from uuid import UUID

from app.domain.list.entity import TaskList as TaskListEntity


class TaskListAll(ABC):

    @abstractmethod
    async def execute(self) -> TaskListEntity:
        pass


class TaskListGet(ABC):

    @abstractmethod
    async def execute(self, tasklist_id: UUID) -> TaskListEntity:
        pass


class TaskListCreate(ABC):

    @abstractmethod
    async def execute(self, entity: TaskListEntity) -> TaskListEntity:
        pass


class TaskListUpdate(ABC):

    @abstractmethod
    async def execute(
        self, tasklist_id: UUID, entity: TaskListEntity
    ) -> TaskListEntity:
        pass


class TaskListDelete(ABC):

    @abstractmethod
    async def execute(self, tasklist_id: UUID) -> None:
        pass
