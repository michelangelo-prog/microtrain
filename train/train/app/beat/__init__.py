from celery import Celery

from train.app.rest import app
from train.domain.config import CeleryConfig

from train.domain.utils import get_train_speed


def make_celery(app):
    celery = Celery(
        app.import_name,
        broker=CeleryConfig.CELERY_BROKER_URL,
        backend=CeleryConfig.CELERY_RESULT_BACKEND,
    )

    celery.conf.beat_schedule = {
        "periodic-task": {
            "task": "periodic.train_speed",
            "args": (dict(actual_speed=get_train_speed()),),
            "schedule": 5.0,
        }
    }

    return celery


celery = make_celery(app)
