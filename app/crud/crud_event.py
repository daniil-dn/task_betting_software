from app.crud.base import CRUDBase
# app
from app.models import Event
from app.schemas import crud_schemas


class CRUDEvent(CRUDBase[Event, crud_schemas.EventCreate, crud_schemas.EventUpdate]):
    pass


crud_event = CRUDEvent(Event)
