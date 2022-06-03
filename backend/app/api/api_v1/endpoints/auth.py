from fastapi import APIRouter, Depends
from starlette import status
from pydantic import UUID4
from typing import Optional
from sqlalchemy.orm import Session
from app import models
from app.api.deps import get_db
from app.core.config import settings
from app import models, schemas, crud

router = APIRouter()


@router.get("/user", status_code=status.HTTP_200_OK)
async def get_user(
        db: Session = Depends(get_db)
):
    user = db.query(models.User).all()
    print("XXXXXXXXXX", user)
    return {"Status": "OK"}


@router.post(
    "/user/create",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.UserResponseAPI
)
async def create_asnumber(
        data: schemas.UserCreateDB,
        db: Session = Depends(get_db),
) -> schemas.UserResponseAPI:
    user = crud.user.create(
        db=db,
        obj_in=data
    )
    print("USER", user)
    return schemas.UserResponseAPI.from_orm(user)
