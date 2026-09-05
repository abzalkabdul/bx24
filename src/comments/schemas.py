from datetime import datetime

from pydantic import BaseModel, ConfigDict


class CommentResponse(BaseModel):
    comment_uuid: str
    body: str
    contact_uuid: str | None = None
    deal_uuid: str | None = None
    author: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class CommentDataSchema(BaseModel):
    body: str
