from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.infrastructure.database.postgres.base import SessionLocal
from app.schemas import Task as TaskSchema
from app.schemas import TaskCreate as TaskCreateSchema
from app.infrastructure.database.models.base import Task as TaskModel


def init_app() -> FastAPI:
    app = FastAPI()

    origins = ["http://localhost", "http://localhost:8080"]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app


app = init_app()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def hello_world():
    return {"Hello": "Erick"}


@app.get("/tasks")
async def get_tasks(db: Session = Depends(get_db)) -> list[TaskSchema]:
    return db.execute(select(TaskModel)).scalars().all()


@app.post("/tasks")
async def create_tasks(
    data: TaskCreateSchema, db: Session = Depends(get_db)
) -> TaskSchema:
    task = TaskModel(**data.model_dump())
    db.add(task)
    db.commit()
    db.refresh(task)

    return task
