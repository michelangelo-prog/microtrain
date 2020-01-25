import os


class CeleryConfig(object):
    """Celery configuration."""

    APP_NAME = os.getenv("APP_NAME", "headquarter")
    CELERY_BROKER_URL = os.getenv("CELERY_BROKER", "redis://redis:6379/0")
    CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND", "redis://redis:6379/0")
