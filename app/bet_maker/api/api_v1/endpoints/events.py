from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core import deps

# app

router = APIRouter()


@router.get("/events", response_model=Any)
async def events(
        db: AsyncSession = Depends(deps.get_db),
) -> Any:
    """
        """
    pass
