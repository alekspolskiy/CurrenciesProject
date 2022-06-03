import logging

from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app import models, crud

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def fill_currencies(db: Session):
    objs = [models.Currency(name=f'currency_{i}', iso=f'i{i}') for i in range(1, 101)]
    objs_ = [models.CurrencyPriceHistory(currency_id=i, price=0) for i, j in enumerate(objs, start=1)]
    crud.currency.create_many(db=db, objs=objs)
    crud.currency_price_history.create_many(db=db, objs=objs_)


def init() -> None:
    db = SessionLocal()
    fill_currencies(db)


def main() -> None:
    logger.info("Filling currencies")
    init()
    logger.info("Filled")


if __name__ == "__main__":
    main()
