from typing import Any

from fastapi import APIRouter

# app

router = APIRouter()


@router.get("/events", response_model=Any)
async def events(
        message_in: Any
) -> Any:
    """
        """
    pass
