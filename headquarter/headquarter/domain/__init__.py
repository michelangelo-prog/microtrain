from headquarter.domain.config import CeleryConfig
from celery import Celery


def create_app():
    app = Celery(
        CeleryConfig.APP_NAME,
        broker=CeleryConfig.CELERY_BROKER_URL,
        backend=CeleryConfig.CELERY_RESULT_BACKEND,
    )
    return app
