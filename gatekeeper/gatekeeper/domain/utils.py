from gatekeeper.domain import db
from gatekeeper.domain.models.barriers import Barrier
from gatekeeper.domain.models.stations import Station

STATIONS = (
    "Wałcz",
    "Ostrowiec Wałecki",
    "Wiesiołka",
    "Zabrodzie",
    "Płytnica",
    "Łowisko",
    "Tarnówka",
    "Węgierce",
    "Annopole",
    "Klukowo",
    "Złotów",
    "Mogilno",
    "Sucharzewo",
    "Mokre",
    "Sławno",
    "Radosław Sławieński",
    "Staniewice",
    "Postomino",
    "Złakowo",
    "Duninowo",
)


def fetch_stations_data():
    for name in STATIONS:
        station = Station(name=name)
        barrier = Barrier()
        station.barrier = barrier
        db.session.add(station)

    db.session.commit()
