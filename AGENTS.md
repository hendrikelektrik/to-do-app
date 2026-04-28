# AGENTS.md

## Run
```bash
uvicorn main:app --reload --port 8000
```

## Verify
Open `http://localhost:8000` - should load UI and display tasks.

## Gotchas
- **CORS required**: Browser makes cross-origin requests. Add `CORSMiddleware` or OPTIONS/POST fail (405 errors).
- **Static files**: FastAPI doesn't serve HTML by default. Mount `StaticFiles` and add route `/` returning `FileResponse("index.html")`.
- **Data model**: Uses UUID, not int. `SPEC.md` updated to reflect this.
- **Persistence**: No `tasks.json` = empty DB; app creates sample task on first run.
- **Write failures**: Silently ignored - no error feedback to user.