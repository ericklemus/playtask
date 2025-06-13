from sqlalchemy.orm import Session

from app.application.list.usecase import (
    TaskListAll as TaskListAllUsecase,
    TaskListGet as TaskListGetUsecase,
    TaskListCreate as TaskListCreateUsecase,
    TaskListUpdate as TaskListUpdateUsecase,
    TaskListDelete as TaskListDeleteUsecase,
)
from app.infrastructure.database.postgres.repositories.list.repository import (
    TaskList as TaskListRepository,
)


def tasklist_all(db_session: Session) -> TaskListAllUsecase:
    return TaskListAllUsecase(TaskListRepository(db_session))


def tasklist_get(db_session: Session) -> TaskListGetUsecase:
    return TaskListGetUsecase(TaskListRepository(db_session))


def tasklist_create(db_session: Session) -> TaskListCreateUsecase:
    return TaskListCreateUsecase(TaskListRepository(db_session))


def tasklist_update(db_session: Session) -> TaskListUpdateUsecase:
    return TaskListUpdateUsecase(TaskListRepository(db_session))


def tasklist_delete(db_session: Session) -> TaskListDeleteUsecase:
    return TaskListDeleteUsecase(TaskListRepository(db_session))
