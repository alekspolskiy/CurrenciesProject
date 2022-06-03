from typing import Optional

from pydantic import UUID4

from app.crud.base import CRUDBase
from app import models, schemas
from sqlalchemy.orm import Session


class CurrencyCRUD(
    CRUDBase[
        models.Currency,
        schemas.CurrencyCreateDB,
        schemas.CurrencyUpdateDB
    ]
):
    """
    Currency CRUD
    """
    pass


class CurrencyPriceHistoryCRUD(
    CRUDBase[
        models.CurrencyPriceHistory,
        schemas.CurrencyPriceHistoryCreateDB,
        schemas.CurrencyPriceHistoryUpdateDB
    ]
):
    """
    Currency price history CRUD
    """

    pass


currency = CurrencyCRUD(models.Currency)
currency_price_history = CurrencyPriceHistoryCRUD(models.CurrencyPriceHistory)
