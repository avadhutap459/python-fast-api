from fastapi import FastAPI

from app.routers.employee import router


app = FastAPI(
    title="FastAPI SQL Server API",
    version="1.0.1"
)


app.include_router(router)


@app.get("/")
def root():

    return {
        "message": "Hello Sir Item : FastAPI SQL Server API is running"
    }
