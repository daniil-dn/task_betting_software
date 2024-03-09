from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.bet_maker.schemas import api_schemas
from app.core import deps
from app.crud import crud_bet
from app.schemas import crud_schemas

# app

router = APIRouter()


@router.post("/bet")
async def bet(
        message_in: api_schemas.BetCreateAPI,
        db: AsyncSession = Depends(deps.get_db),
) -> Any:
    await crud_bet.create(db, obj_in=crud_schemas.BetCreate(**message_in.model_dump()))


@router.get("/bet")
async def bet(
) -> Any:
    """
        """
    pass
