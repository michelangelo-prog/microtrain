from celery import Celery

from train.app.rest import app
from train.domain.config import CeleryConfig, CeleryHeadquarterConfig

from train.domain.utils import get_train_speed, get_train_station


from celery.decorators import periodic_task
from datetime import timedelta


def make_celery(app):
    celery = Celery(
        app.import_name,
        broker=CeleryConfig.CELERY_BROKER_URL,
        backend=CeleryConfig.CELERY_RESULT_BACKEND,
    )

    return celery

def make_celery_headquarter(app):
    celery = Celery(
        app.import_name,
        broker=CeleryHeadquarterConfig.CELERY_BROKER_URL,
        backend=CeleryHeadquarterConfig.CELERY_RESULT_BACKEND,
    )

    return celery


celery = make_celery(app)
celery_headquarter = make_celery_headquarter(app)


@periodic_task(run_every=timedelta(seconds=10))
def train_speed():
    celery_headquarter.send_task(
        "periodic.train_speed",
        (dict(actual_speed=get_train_speed()),)
    )

@periodic_task(run_every=timedelta(seconds=30))
def train_station():
    celery_headquarter.send_task(
        "periodic.train_station",
        (dict(train_station=get_train_station()),)
    )



