from sqlalchemy.orm import Session

from app.application.task.usecase import (
    TaskAll as TaskAllUsecase,
    TaskGet as TaskGetUsecase,
    TaskCreate as TaskCreateUsecase,
    TaskUpdate as TaskUpdateUsecase,
    TaskDelete as TaskDeleteUsecase,
)
from app.infrastructure.database.postgres.repositories.task.repository import (
    Task as TaskRepository,
)


def task_all(db_session: Session) -> TaskAllUsecase:
    return TaskAllUsecase(TaskRepository(db_session))


def task_get(db_session: Session) -> TaskGetUsecase:
    return TaskGetUsecase(TaskRepository(db_session))


def task_create(db_session: Session) -> TaskCreateUsecase:
    return TaskCreateUsecase(TaskRepository(db_session))


def task_update(db_session: Session) -> TaskUpdateUsecase:
    return TaskUpdateUsecase(TaskRepository(db_session))


def task_delete(db_session: Session) -> TaskDeleteUsecase:
    return TaskDeleteUsecase(TaskRepository(db_session))
