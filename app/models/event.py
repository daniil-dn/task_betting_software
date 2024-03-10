from datetime import datetime

from sqlalchemy import Column, DateTime, BigInteger, ForeignKey, Float

from app.db.base_class import Base
from app.models.model_base import ModelBase


class Event(Base, ModelBase):
    id = Column(BigInteger, primary_key=True, index=True)
    status_id = Column(BigInteger, ForeignKey('event_status.id'), nullable=True)
    coefficient = Column(Float, nullable=False)
    deadline_dt = Column(DateTime(timezone=True), nullable=True)
    updated_at = Column(DateTime(timezone=True), onupdate=datetime.utcnow)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
