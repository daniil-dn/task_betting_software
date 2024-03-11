from fastapi import APIRouter

from app.bet_maker.api.api_v1.endpoints import bet, events, callback

api_router = APIRouter()
api_router.include_router(bet.router, prefix="", tags=["bet"])
api_router.include_router(events.router, prefix="", tags=["events"])
api_router.include_router(callback.router, prefix="/callback", tags=["callback"])
