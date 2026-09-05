import uvicorn

from fastapi import FastAPI
from src.auth.router import router as auth_router
from src.users.router import router as user_router
from src.comments.router import router as comment_router

from src.users.models import Users
from src.contacts.models import Contacts
from src.deals.models import Deals
from src.pipeline_stages.models import PipelineStages
from src.tasks.models import Tasks
from src.comments.models import Comments
from src.notifications.models import Notifications
from src.tg_sessions.models import TgSessions
from src.auth.models import TokenBlacklist
app = FastAPI()

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(comment_router)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8001)
