from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship

from gatekeeper.domain import db
from gatekeeper.domain.models.barriers import Barrier
from gatekeeper.domain.models.behaviors import IdMixin


class Station(IdMixin, db.Model):
    __tablename__ = "stations"

    name = Column(String(120), unique=True, nullable=False)
    barrier_id = Column(Integer, ForeignKey("barriers.id"), nullable=False, unique=True)

    barrier = relationship(Barrier, backref=backref("station", uselist=False))
