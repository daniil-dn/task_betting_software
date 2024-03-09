import json
from typing import Any

import aiohttp
from fastapi import APIRouter

# app

router = APIRouter()


@router.get("/events", response_model=Any)
async def events(
) -> Any:
    """
        """
    async with aiohttp.ClientSession() as session:
        async with session.get("http://localhost:9091/api/v1/events") as response:
            content = await response.content.read()
    return json.dumps(content)
