from typing import Optional

from pydantic import UUID4

from app.crud.base import CRUDBase
from app import models, schemas
from sqlalchemy.orm import Session


class UserCRUD(
    CRUDBase[
        models.User,
        schemas.UserCreateDB,
        schemas.UserCreateDB
    ]
):
    """
    User CRUD
    """
    pass


user = UserCRUD(models.User)
