from flask import Blueprint, abort, request
from marshmallow import Schema, fields

from gatekeeper.domain import db
from gatekeeper.domain.decorators import request_schema
from gatekeeper.domain.models.stations import Station, StationDoesNotExist

barrier_blueprint = Blueprint("barrier", __name__)


class BarrierStatusRequestSchema(Schema):
    station = fields.Str(required=True)
    barrier_status = fields.Str(required=True)


def raise_KeyError(msg=""):
    raise KeyError(msg)


@barrier_blueprint.route("/barrier", methods=["GET"])
def get_barrier_status():
    try:
        station_name = request.args.get("station") or raise_KeyError()
        barrier_status = Station.get_barrier_status_by_station_name(
            station_name=station_name
        )
        return {"status": barrier_status}, 200
    except StationDoesNotExist:
        return abort(404)
    except KeyError:
        return {"info": "Provide parameter 'station'"}, 400


@barrier_blueprint.route("/barrier", methods=["POST"])
@request_schema(BarrierStatusRequestSchema)
def change_barrier_status(json_data):
    try:
        station = Station.change_barrier_status_at_station_by_station_name(
            json_data["station"], json_data["barrier_status"]
        )
        db.session.add(station)
        db.session.commit()
        return {"status": "success"}, 201
    except StationDoesNotExist:
        return abort(404)
    except KeyError:
        return {"info": "Wrong parameter 'barrier_status'"}, 400
