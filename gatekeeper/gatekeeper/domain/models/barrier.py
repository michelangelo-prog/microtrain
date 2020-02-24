from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from gatekeeper.domain import db
from gatekeeper.domain.models.behaviors import IdMixin


class Barrier(IdMixin, db.Model):
    __tablename__ = "barrier"

    name = Column(String(120), unique=True, nullable=False)

    barrier_status = relationship("BarrierStatus", uselist=False, backref="barrier")
