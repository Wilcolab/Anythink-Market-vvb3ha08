"""Python FastAPI Server - Task Management API

This module provides a RESTful API for managing tasks using FastAPI.
It runs on port 8000 and provides endpoints for creating and retrieving tasks.

Endpoints:
    GET  /       - Health check endpoint
    GET  /tasks  - Retrieve all tasks
    POST /tasks  - Add a new task

The server uses Uvicorn with auto-reload for development.
"""

from fastapi import FastAPI
from pydantic import BaseModel

# Initialize FastAPI application
app = FastAPI()

# Pydantic model for task validation
class Task(BaseModel):
    """Task model for API request validation.
    
    Attributes:
        text (str): The task description text
    """
    text: str

# In-memory storage for tasks (for demo purposes)
# TODO: Replace with database in production
tasks = [
    "Write a diary entry from the future",
    "Create a time machine from a cardboard box",
    "Plan a trip to the dinosaurs",
    "Draw a futuristic city",
    "List items to bring on a time-travel adventure"
]

@app.get("/")
def health_check():
    """Health check endpoint.
    
    Returns:
        str: Simple message indicating the server is running
    """
    return "Hello World"

@app.post("/tasks")
def add_task(task: Task):
    """Add a new task to the task list.
    
    Args:
        task (Task): Task object containing the task text
        
    Returns:
        dict: Success message confirming task addition
    """
    tasks.append(task.text)
    return {"message": "Task added successfully"}

@app.get("/tasks")
def get_all_tasks():
    """Retrieve all tasks from the task list.
    
    Returns:
        dict: Dictionary containing the list of all tasks
    """
    return {"tasks": tasks}
