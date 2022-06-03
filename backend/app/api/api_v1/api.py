from fastapi import APIRouter

from app.api.api_v1.endpoints import auth
from app.api.api_v1.endpoints import currency
from app.api.api_v1.endpoints import utils
from app.api.api_v1.endpoints import exchange
from app.core.config import settings

api_router = APIRouter()
api_router.include_router(auth.router, prefix='/auth', tags=["auth"])
api_router.include_router(currency.router, prefix='/currency', tags=['currency'])
api_router.include_router(utils.router, prefix='/utils', tags=['utils'])
api_router.include_router(exchange.router, prefix='/exchange', tags=['exchange'])
