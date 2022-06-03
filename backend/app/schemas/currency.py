from pydantic.main import BaseModel
from datetime import datetime
from typing import Optional, Any
from pydantic import UUID4, EmailStr, root_validator
from app import models
from app.core.security import get_password_hash


class CurrencyCreateDB(BaseModel):
    name: str
    iso: str
    price: float = 0


class CurrencyUpdateDB(BaseModel):
    name: Optional[str]
    iso: Optional[str]
    price: Optional[float]


class CurrencyResponseAPI(BaseModel):
    unique_id: UUID4
    dt_create: datetime
    dt_update: datetime
    name: str
    iso: str
    price: float

    class Config:
        orm_mode = True

    @classmethod
    def create_for_currency(cls, currency: "models.Currency"):
        data = {
            'unique_id': currency.unique_id,
            'dt_create': currency.dt_create,
            'dt_update': currency.dt_update,
            'name': currency.name,
            'iso': currency.iso,
            'price': currency.actual_price,
        }
        return cls(**data)

    @classmethod
    def create_for_history(cls, currency_history: "models.CurrencyPriceHistory"):
        data = {
            'unique_id': currency_history.unique_id,
            'dt_create': currency_history.dt_create,
            'dt_update': currency_history.dt_update,
            'name': currency_history.currency_name,
            'iso': currency_history.currency_iso,
            'price': currency_history.price,
        }
        return cls(**data)


class CurrencyPriceHistoryCreateDB(BaseModel):
    currency_id: int
    price: float = 0


class CurrencyPriceHistoryUpdateDB(BaseModel):
    currency_id: Optional[int]
    price: Optional[float]


class CurrencyPriceHistoryResponseAPI(BaseModel):
    unique_id: UUID4
    dt_create: datetime
    dt_update: datetime
    currency_id: int
    price: float

    class Config:
        orm_mode = True
