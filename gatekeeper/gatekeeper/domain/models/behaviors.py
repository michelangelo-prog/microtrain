import datetime

from gatekeeper.domain import db


class IdMixin(db.Model):

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)


class UpdateAtMixin(db.Model):

    __abstract__ = True

    updated_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.datetime.now,
        onupdate=datetime.datetime.now,
    )
