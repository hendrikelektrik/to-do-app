# To-Do App

FastAPI to-do app with CRUD operations.

## Run

```bash
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

Open http://localhost:8000

## Features

- Create, read, update, delete tasks
- Persistent storage in tasks.json
- Web UI included

## Tech

- FastAPI
- Vanilla JS/HTML

## Walkthrough

This app was built with OpenCode - an AI coding agent.

### Issues Fixed

1. **UI not loading** - FastAPI doesn't serve HTML by default
   - Solution: Mount StaticFiles and add route `/` returning FileResponse

2. **Tasks not displaying** - Data model used int but code used UUID
   - Solution: Added sample task creation on first run

3. **Tasks not saving** - CORS blocked browser requests
   - Solution: Added CORSMiddleware

### Improvements Made

- Relative API URL instead of hardcoded localhost
- Input validation with max length
- Error handling with try/catch
- Loading states while API calls
- Fixed HTML escaping for XSS prevention
- Updated SPEC.md to match code (UUID)

### Commands Used

- `opencode "review my project"` - Initial review
- `opencode "fix the bugs"` - Fixed CORS and static files
- `opencode "suggest improvements"` - Security/UX improvements