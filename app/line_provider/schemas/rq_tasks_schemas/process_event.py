from pydantic import BaseModel


class ProcessEventTask(BaseModel):
    event_id: int
    status_ids: list[int]
