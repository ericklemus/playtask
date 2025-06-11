from fastapi import FastAPI, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.schemas import Task as TaskSchema
from app.schemas import TaskCreate as TaskCreateSchema
from app.models import Task as TaskModel

app = FastAPI()

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
async def get_tasks(
    db: Session = Depends(get_db)
) -> list[TaskSchema]:
    return db.execute(
        select(TaskModel)
    ).scalars().all()

@app.post("/tasks")
async def create_tasks(
    data: TaskCreateSchema,
    db: Session = Depends(get_db)
) -> TaskSchema:
    task = TaskModel(**data.model_dump())
    db.add(task)
    db.commit()
    db.refresh(task)

    return task