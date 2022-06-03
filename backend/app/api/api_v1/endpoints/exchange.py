from fastapi import Request, APIRouter, Depends
from starlette import status
from sse_starlette.sse import EventSourceResponse
from app.sse.sse_helper import SseHelper
from app.api.deps import get_db
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/start", status_code=status.HTTP_200_OK)
async def message_stream(
        request: Request,
        db: Session = Depends(get_db)
):
    sse = SseHelper(request=request, db=db).run_loop()
    return EventSourceResponse(sse)
