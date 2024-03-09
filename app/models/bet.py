import datetime

from sqlalchemy import Column, DateTime, BigInteger, ForeignKey

from app.db.base_class import Base
from app.models.model_base import ModelBase


class Bet(Base, ModelBase):
    id = Column(BigInteger, primary_key=True, index=True)
    event_id = Column(BigInteger, ForeignKey("event.id"), nullable=False)
    status_id = Column(BigInteger, ForeignKey("bet_status.id"), nullable=False)
    amount = Column(BigInteger, nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=datetime.datetime.utcnow)
    created_at = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)
