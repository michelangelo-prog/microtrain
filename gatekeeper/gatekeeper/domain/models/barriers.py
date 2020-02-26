from sqlalchemy import Boolean, Column

from gatekeeper.domain import db
from gatekeeper.domain.models.behaviors import IdMixin, UpdateAtMixin


class Barrier(IdMixin, UpdateAtMixin, db.Model):
    __tablename__ = "barriers"

    is_open = Column(Boolean, unique=False, default=True, nullable=False)
