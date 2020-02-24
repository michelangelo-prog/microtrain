from sqlalchemy import Boolean, Column, ForeignKey, Integer

from gatekeeper.domain import db
from gatekeeper.domain.models.behaviors import UpdateAtMixin


class BarrierStatus(UpdateAtMixin, db.Model):
    __tablename__ = "barrier_status"

    barrier_id = Column(Integer, ForeignKey("barrier.id"), primary_key=True)
    is_open = Column(Boolean, unique=False, default=True, nullable=False)
