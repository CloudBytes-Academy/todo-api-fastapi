from fastapi import FastAPI
from datetime import datetime
from typing import Optional

from fastapi.encoders import jsonable_encoder
from model.model import Task, TaskList
import model.taskman as taskman

app = FastAPI()


@app.get("/api/tasks")
async def get_tasks():
    """TODO
    Fetch the list of all tasks
    """
    return "TODO"


@app.get("/api/tasks/{id}")
async def get_task(id: int):
    """TODO
    Fetch the task by id
    """
    return "TODO"


@app.post("/api/tasks/create")
async def create_task(task: Task):
    """TODO
    1. Create a new task and
    2. Return the details of task
    """
    return "TODO"


@app.put("/api/tasks/{id}/update")
async def update_task(id: int, task: Task):
    """TODO
    1. Update the task by id
    2. Return the updated task
    """
    return "TODO"


@app.delete("/api/tasks/{id}/delete")
async def delete_task(id: int):
    """TODO
    1. Delete the task by id
    2. Return a confirmation of deletion
    """
    return "TODO"
