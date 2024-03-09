from typing import Any

from fastapi import APIRouter

# app

router = APIRouter()


@router.post("/", response_model=Any)
async def test(
        message_in: Any
) -> Any:
    """
        """
    pass
