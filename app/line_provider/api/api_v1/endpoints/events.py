from fastapi import APIRouter, HTTPException, Path

# app

router = APIRouter()


@router.put('/event')
async def create_event():
    pass


@router.get('/event/{event_id}')
async def get_event(event_id: str = Path(ge=1)):
    # if event_id in events:
    #     return events[event_id]

    raise HTTPException(status_code=404, detail="Event not found")


@router.get('/events')
async def get_events():
    pass
