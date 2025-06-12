from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.infrastructure.database.models.base import TaskList as TaskListModel
from app.infrastructure.database.postgres.base import get_db
from app.presentation.api.resources.list.dtos import (
    TaskListGetResponse as TaskListGetResponseDTO,
)
from app.presentation.api.resources.list.dtos import (
    TaskListCreatePayload as TaskListCreatePayloadDTO,
)
from app.presentation.api.resources.list.dtos import (
    TaskListCreateResponse as TaskListCreateResponseDTO,
)
from app.presentation.api.resources.list.dtos import (
    TaskListUpdatePayload as TaskListUpdatePayloadDTO,
)
from app.presentation.api.resources.list.dtos import (
    TaskListUpdateResponse as TaskListUpdateResponseDTO,
)
from app.presentation.api.resources.list.dtos import (
    TaskListDeleteResponse as TaskListDeleteResponseDTO,
)

tasklist_router = APIRouter(prefix="", tags=["lists"])


@tasklist_router.get(
    "/tasklist",
    response_model=list[TaskListGetResponseDTO],
    status_code=status.HTTP_200_OK,
)
async def tasklist_all(db: Session = Depends(get_db)) -> list[TaskListGetResponseDTO]:
    return db.execute(select(TaskListModel)).scalars().all()


@tasklist_router.get(
    "/tasklist/{uuid}",
    response_model=TaskListGetResponseDTO,
    status_code=status.HTTP_200_OK,
)
async def tasklist_get(
    uuid: UUID, db: Session = Depends(get_db)
) -> TaskListGetResponseDTO:
    tasklist = db.execute(
        select(TaskListModel).where(TaskListModel.uuid == uuid)
    ).scalar_one_or_none()

    if tasklist is None:
        raise HTTPException(status_code=404, detail="TaskList not found")

    return tasklist


@tasklist_router.post(
    "/tasklist",
    response_model=TaskListCreateResponseDTO,
    status_code=status.HTTP_201_CREATED,
)
async def tasklist_create(
    data: TaskListCreatePayloadDTO, db: Session = Depends(get_db)
) -> TaskListCreateResponseDTO:
    tasklist = TaskListModel(**data.model_dump())
    db.add(tasklist)
    db.commit()
    db.refresh(tasklist)

    return tasklist


@tasklist_router.put(
    "/tasklist/{uuid}",
    response_model=TaskListUpdateResponseDTO,
    status_code=status.HTTP_201_CREATED,
)
async def tasklist_update(
    uuid: UUID,
    data: TaskListUpdatePayloadDTO,
    db: Session = Depends(get_db),
) -> TaskListUpdateResponseDTO:
    tasklist = db.execute(
        select(TaskListModel).where(TaskListModel.uuid == uuid)
    ).scalar_one_or_none()

    if tasklist is None:
        raise HTTPException(status_code=404, detail="TaskList not found")

    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(tasklist, key, value)

    db.add(tasklist)
    db.commit()
    db.refresh(tasklist)

    return tasklist


@tasklist_router.delete(
    "/tasklist/{uuid}",
    response_model=TaskListDeleteResponseDTO,
    status_code=status.HTTP_200_OK,
)
async def tasklist_delete(
    uuid: UUID,
    db: Session = Depends(get_db),
) -> TaskListDeleteResponseDTO:
    tasklist = db.execute(
        select(TaskListModel).where(TaskListModel.uuid == uuid)
    ).scalar_one_or_none()

    if tasklist is None:
        raise HTTPException(status_code=404, detail="TaskList not found")

    db.delete(tasklist)
    db.commit()

    return {"msg": "Tasklist deleted"}
