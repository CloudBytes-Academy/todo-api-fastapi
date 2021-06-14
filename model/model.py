from pydantic import BaseModel
from datetime import datetime
from typing import NewType, Optional


ID = NewType("id", int)


class Task(BaseModel):
    summary: str
    priority: int
    # due_date: Optional[datetime]


class TaskList(BaseModel):
    id: ID
    task: Task
