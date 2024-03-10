from app.crud.base import CRUDBase
# app
from app.models import EventStatus
from app.schemas import crud_schemas


class CRUDEventStatus(
    CRUDBase[
        EventStatus,
        crud_schemas.EventStatusCreate,
        crud_schemas.EventUpdate]
):
    pass


crud_event_status = CRUDEventStatus(EventStatus)
