import uvicorn

from fastapi import FastAPI
from src.auth.router import router as auth_router
from src.users.router import router as user_router
app = FastAPI()

app.include_router(auth_router)
app.include_router(user_router)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8001)
