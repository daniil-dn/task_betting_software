import json
from typing import Any, List

import aiohttp
from fastapi import APIRouter

from app.bet_maker.schemas import api_schemas

# app

router = APIRouter()


@router.get("/events", response_model=List[api_schemas.EventGet])
async def events(
) -> Any:
    """
        """
    async with aiohttp.ClientSession(trust_env=True) as session:
        async with session.get("http://app_line_provider:9090/api/v1/events") as response:
            content = await response.content.read()
    return json.loads(content.decode('utf-8'))
