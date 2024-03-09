from fastapi import APIRouter

from app.bet_maker.api.api_v1.endpoints import bet, events

api_router = APIRouter()
api_router.include_router(bet.router, prefix="", tags=["bet"])
api_router.include_router(events.router, prefix="", tags=["events"])
