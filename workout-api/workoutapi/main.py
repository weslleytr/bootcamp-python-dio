from fastapi import FastAPI
from routes import api_router
from fastapi_pagination import add_pagination

app = FastAPI(title="WorkoutAPI")
add_pagination(app)
app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run('main:app', host="0.0.0.0", port=8000, log_level="info", reload=True)