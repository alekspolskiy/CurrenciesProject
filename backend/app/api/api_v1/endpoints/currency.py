from fastapi import APIRouter, Depends
from fastapi_pagination import Page, paginate, Params
from starlette import status
from app import crud, schemas
from app.api.deps import get_db
from sqlalchemy.orm import Session


router = APIRouter()


@router.get("/list", status_code=status.HTTP_200_OK, response_model=Page[schemas.CurrencyResponseAPI])
async def get_currencies(
        db: Session = Depends(get_db),
        params: Params = Depends(),
):
    result = []
    currencies = crud.currency.get_all(db)
    for currency in currencies:
        result.append(schemas.CurrencyResponseAPI.create_for_currency(currency))
    return paginate(result, params)


@router.get("/history", status_code=status.HTTP_200_OK, response_model=Page[schemas.CurrencyResponseAPI])
async def get_currencies_history(
        db: Session = Depends(get_db),
        params: Params = Depends(),
):
    result = []
    currencies_history = crud.currency_price_history.get_all(db)
    for item in currencies_history:
        result.append(schemas.CurrencyResponseAPI.create_for_history(item))
    return paginate(result, params)
