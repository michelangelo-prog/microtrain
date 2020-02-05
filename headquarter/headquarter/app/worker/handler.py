from headquarter.app.worker import make_worker

worker = make_worker()


@worker.task(name="periodic.train_speed")
def train_speed(data):
    print("Train speed {}".format(data["actual_speed"]))
