# To-Do App Specification

## Project: FastAPI To-Do App

### Features
- Create task (title, description, completed status)
- Read/List all tasks
- Update task (toggle complete, edit title/description)
- Delete task

### API Endpoints
- `GET /tasks` - List all tasks
- `POST /tasks` - Create new task
- `GET /tasks/{id}` - Get single task
- `PUT /tasks/{id}` - Update task
- `DELETE /tasks/{id}` - Delete task

### Data Model
```python
Task:
  - id: UUID (auto-generated)
  - title: str
  - description: str (optional)
  - completed: bool (default False)
```