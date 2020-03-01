from flask import Blueprint, request

from gatekeeper.domain.models.stations import Station, StationDoesNotExist

barrier_blueprint = Blueprint("barrier", __name__)


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
        return {"info": "Station does not exists"}, 400
    except KeyError:
        return {"info": "Provide parameter 'station'"}, 400
