from celery import Celery

from headquarter.domain.config import CeleryConfig


def make_worker():
    worker = Celery(
        CeleryConfig.APP_NAME,
        broker=CeleryConfig.CELERY_BROKER_URL,
        backend=CeleryConfig.CELERY_RESULT_BACKEND,
    )
    return worker
