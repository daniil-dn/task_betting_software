import datetime

from sqlalchemy import Column, DateTime, BigInteger, ForeignKey, Float

from app.db.base_class import Base
from app.models.model_base import ModelBase


class Event(Base, ModelBase):
    id = Column(BigInteger, primary_key=True, index=True)
    status_id = Column(ForeignKey('event_status.id'), nullable=True)
    coefficient = Column(Float, nullable=False)
    deadline = Column(DateTime(timezone=True))
    updated_at = Column(DateTime(timezone=True), onupdate=datetime.datetime.utcnow)
    created_at = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)
