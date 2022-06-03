from fastapi import APIRouter, Depends
from starlette import status
from app import crud, models
from app.api.deps import get_db
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/fill_currencies", status_code=status.HTTP_200_OK)
async def fill_currencies(
        db: Session = Depends(get_db)
):
    objs = [models.Currency(name=f'currency_{i}', iso=f'i{i}') for i in range(1, 101)]
    objs_ = [models.CurrencyPriceHistory(currency_id=i, price=0) for i, j in enumerate(objs, start=1)]
    crud.currency.create_many(db=db, objs=objs)
    crud.currency_price_history.create_many(db=db, objs=objs_)
