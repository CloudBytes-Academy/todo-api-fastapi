from fastapi import FastAPI
from datetime import datetime
from typing import Optional

from fastapi.encoders import jsonable_encoder
from starlette.responses import Response
from model.model import Task, TaskList
import model.taskman as taskman

app = FastAPI()


@app.get("/api/tasks")
async def get_tasks():

    return taskman.get_tasks()


@app.get("/api/tasks/{id}")
async def get_task(id: int):

    return taskman.get_tasks(id)


@app.post("/api/tasks/create")
async def create_task(task: Task):
    id = taskman.create_task(task)

    return taskman.get_tasks(id)


@app.put("/api/tasks/{id}/update")
async def update_task(id: int, task: Task):

    taskman.update_task(id, task)
    return taskman.get_tasks(id)


@app.delete("/api/tasks/{id}/delete")
async def delete_task(id: int):
    id = taskman.delete_task(id)
    response = {id: "Task successfully deleted"}
    return jsonable_encoder(response)
