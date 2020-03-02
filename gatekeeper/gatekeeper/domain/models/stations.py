from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship

from gatekeeper.domain import db
from gatekeeper.domain.models.barriers import Barrier
from gatekeeper.domain.models.behaviors import IdMixin

BARRIER_STATUS = {"open": True, "closed": False}


class StationDoesNotExist(Exception):
    """Raise when Station does not exists."""

    pass


class Station(IdMixin, db.Model):
    __tablename__ = "stations"

    name = Column(String(120), unique=True, nullable=False)
    barrier_id = Column(Integer, ForeignKey("barriers.id"), nullable=False, unique=True)

    barrier = relationship(Barrier, backref=backref("station", uselist=False))

    @classmethod
    def get_barrier_status_by_station_name(cls, station_name):
        station = cls.get_station_by_name_or_raise_exception(station_name)
        return station.get_barrier_status()

    @classmethod
    def get_station_by_name_or_raise_exception(cls, station_name):
        station = cls.get_station_by_name(station_name)
        if not station:
            raise StationDoesNotExist
        return station

    @classmethod
    def get_station_by_name(cls, name):
        return cls.query.filter_by(name=name).one_or_none()

    def get_barrier_status(self):
        return "open" if self.barrier.is_open else "closed"

    @classmethod
    def change_barrier_status_at_station_by_station_name(
        cls, station_name, barrier_status
    ):
        station = cls.get_station_by_name_or_raise_exception(station_name)
        station.barrier.is_open = BARRIER_STATUS[barrier_status]
        return station
