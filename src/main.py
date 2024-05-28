from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from sqlmodel import Field, Session, SQLModel, create_engine, select
import os
from dotenv import load_dotenv
# import psycopg2 as pg

load_dotenv()

class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    done: Optional[bool] = Field(default=False)



api = FastAPI()

engine = create_engine(
    f"{os.getenv('DATABASE_URL')}"
)


@api.on_event("startup")
def run_migrations():
    SQLModel.metadata.create_all(engine)


@api.get("/")
def list() -> list[Task]:
    with Session(engine) as session:
        return session.exec(
            select(Task)
            ).all()


@api.post("/")
def create(task: Task):
    with Session(engine) as session:
        session.add(task)
        session.commit()
        session.refresh(task)
        return task


class TaskUpdatePayload(BaseModel):
    name: str
    done: Optional[bool] = Field(default=False)


@api.patch("/{task_id}")
def update(task_id: int, body: TaskUpdatePayload):
    with Session(engine) as session:
        task = session.exec(select(Task).where(Task.id == task_id)).one()
        task.done = body.done
        session.commit()
        session.refresh(task)
        return task
