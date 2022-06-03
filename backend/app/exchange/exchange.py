from sqlalchemy.orm import Session
from random import random
from app import crud, models


class ExchangeHandler:

    def __init__(self, db: Session):
        self.db = db
        self.currencies = self.prepare_biding_data()

    def prepare_biding_data(self):
        return crud.currency.get_all(db=self.db)

    async def make_biding(self, currencies):
        if not currencies:
            currencies = [
                    {
                        'currency_id': currency.id,
                        'currency_name': currency.name,
                        'currency_iso': currency.iso,
                        'price': self.get_new_price(float(currency.price)),
                    }
                    for currency in self.currencies
                ]
        else:
            _ = [currency.update({'price': self.get_new_price(currency['price'])}) for currency in currencies]
        await self.update_price_history(currencies)
        return currencies

    async def update_price_history(self, currencies):
        objs = [models.CurrencyPriceHistory(currency_id=currency['currency_id'], price=currency['price'])
                for currency in currencies]
        crud.currency_price_history.create_many(
            db=self.db,
            objs=objs
        )

    def get_new_price(self, price):
        movement = -1 if random() < 0.5 else 1
        return price + movement
