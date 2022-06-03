from pydantic.main import BaseModel
from datetime import datetime
from typing import Optional, Any
from pydantic import UUID4, EmailStr, root_validator

from app.core.security import get_password_hash


class UserCreateDB(BaseModel):
    email: EmailStr
    hashed_password: str
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    @root_validator(pre=True)
    def validate_root(cls, values):
        values['hashed_password'] = get_password_hash(values['password'])
        return values


class UserResponseAPI(BaseModel):
    unique_id: UUID4
    dt_create: datetime
    dt_update: datetime
    email: EmailStr
    hashed_password: str
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    class Config:
        orm_mode = True
