from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core import deps
from app.schemas import api_schemas

# app

router = APIRouter()


@router.post("/bet")
async def bet(
        message_in: api_schemas.BetCreateAPI,
        db: AsyncSession = Depends(deps.get_db),
) -> Any:
    return


@router.get("/bet")
async def bet(
) -> Any:
    """
        """
    pass
