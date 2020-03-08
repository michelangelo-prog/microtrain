from headquarter.app.worker import make_worker
from headquarter.domain.handlers.speed_handler import SpeedHandler
from headquarter.domain.handlers.station_handler import StationHandler

worker = make_worker()


@worker.task(name="periodic.train_speed")
def train_speed(data):
    print("Train speed {} - TASK START".format(data["actual_speed"]))
    speed = data.get("actual_speed")
    speed_handler = SpeedHandler()
    speed_handler.save_speed(speed)
    print("Train speed {} - TASK FINISHED".format(data["actual_speed"]))


@worker.task(name="periodic.train_station")
def train_station(data):
    print("Train station {} - TASK START".format(data["train_station"]))
    station_handler = StationHandler()
    station_handler.train_goes_to_station(data["train_station"])
    print("Train station {} - TASK FINISHED".format(data["train_station"]))
