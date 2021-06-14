from model.model import Task, TaskList
import json
from pydantic import parse_file_as
from typing import List, Optional

filepath = "data/tasks.json"


def data_to_json(data: List):
    """
    TODO
    1. Take input data, of a list of tasks
    2. Write the data into a json file (tasks.json)
    """
    pass


def get_tasks(id: Optional[int] = 0):
    """
    TODO
    1. Fetch all tasks if no argument (id) provided
    2. Else fetch the task by id provided
    """
    return "response"


def create_task(new_task: Task):
    """
    TODO:
    1. Create a new task and add it to the list of tasks
    2. Write the updated tasklist to file
    """
    return "id"


def delete_task(id):
    """
    TODO:
    1. Delete the task by id provided
    """
    return "id"


def update_task(id: int, new_task: Task):
    """
    TODO
    1. Update the task by id based on new task details
    2. write the updated tasklist to file
    """
    return "id"
