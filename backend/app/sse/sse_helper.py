import asyncio
import json
from fastapi import Request
from ..exchange.exchange import ExchangeHandler


class SseHelper:
    def __init__(self, request: Request, db):
        self.request = request
        self.db = db

    async def run_loop(self, delay=1):
        handler = ExchangeHandler(
            db=self.db,
        )
        currencies = []
        while True:
            currencies = await handler.make_biding(currencies=currencies)
            if await self.request.is_disconnected():
                break

            if not currencies:
                await asyncio.sleep(delay)
                continue
            yield json.dumps(currencies)
            await asyncio.sleep(delay)
