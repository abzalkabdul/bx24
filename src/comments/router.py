from fastapi import APIRouter, HTTPException, status

from src.comments.models import Comments
from src.comments.schemas import CommentResponse, CommentDataSchema
from src.database import SessionDep

from sqlalchemy import select

router = APIRouter(tags=["Comments"])

@router.get("/{user_id}/comments")
async def get_comments(session: SessionDep):

    try:
        query = await session.execute(select(Comments))
        comments = query.scalars().all()

        return [CommentResponse.model_validate(comment) for comment in comments]

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail="data is not found",
        )

@router.post("/{user_id}/new_comment")
async def create_comment(session: SessionDep,
                         comment_data: CommentDataSchema):

    new_comment = Comments(**comment_data.model_dump())
    session.add(new_comment)
    await session.commit()

    return {"success": "success"}

