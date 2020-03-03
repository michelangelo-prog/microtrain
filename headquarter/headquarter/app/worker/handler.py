from headquarter.app.worker import make_worker
from headquarter.domain.handlers import SpeedHandler

worker = make_worker()


@worker.task(name="periodic.train_speed")
def train_speed(data):
    speed = data.get("actual_speed")
    speed_handler = SpeedHandler()
    speed_handler.save_speed(speed)
    print("Train speed {}".format(data["actual_speed"]))


@worker.task(name="periodic.train_station")
def train_station(data):
    print("Train station {}".format(data["train_station"]))
