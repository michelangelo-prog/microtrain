from celery import Celery

from train.app.rest import app
from train.domain.config import CeleryConfig


def make_celery(app):
    celery = Celery(
        app.import_name,
        broker=CeleryConfig.CELERY_BROKER_URL,
        backend=CeleryConfig.CELERY_RESULT_BACKEND,
    )

    celery.conf.beat_schedule = {
        "see-you-in-ten-seconds-task": {"task": "periodic.see_you", "schedule": 10.0}
    }

    return celery


celery = make_celery(app)
