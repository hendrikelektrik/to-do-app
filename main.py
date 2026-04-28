from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from uuid import UUID, uuid4
import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "tasks.json"

app = FastAPI(title="To-Do API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="."), name="static")

@app.get("/")
def serve_index():
    return FileResponse("index.html")

class Task(BaseModel):
    id: Optional[UUID] = None
    title: str
    description: Optional[str] = None
    completed: bool = False

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

def load_tasks() -> dict[UUID, Task]:
    if DATA_FILE.exists():
        data = json.loads(DATA_FILE.read_text())
        return {UUID(k): Task(**v) for k, v in data.items()}
    return {}

def save_tasks():
    data = {str(k): v.model_dump() for k, v in tasks_db.items()}
    DATA_FILE.write_text(json.dumps(data, default=str))

tasks_db: dict[UUID, Task] = load_tasks()

if not tasks_db:
    sample = Task(title="Welcome to your To-Do App!", description="Add, edit, and complete tasks", completed=False)
    sample.id = uuid4()
    tasks_db[sample.id] = sample
    save_tasks()

@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    task.id = uuid4()
    tasks_db[task.id] = task
    save_tasks()
    return task

@app.get("/tasks", response_model=list[Task])
def list_tasks():
    return list(tasks_db.values())

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: UUID):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks_db[task_id]

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: UUID, task_update: TaskUpdate):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    
    task = tasks_db[task_id]
    if task_update.title is not None:
        task.title = task_update.title
    if task_update.description is not None:
        task.description = task_update.description
    if task_update.completed is not None:
        task.completed = task_update.completed
    
    save_tasks()
    return task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: UUID):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    del tasks_db[task_id]
    save_tasks()
    return {"message": "Task deleted"}