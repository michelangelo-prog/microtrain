import os

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):
    """Base configuration."""

    APP_NAME = os.getenv("APP_NAME", "train")
    REDIS_URL = os.getenv("REDIS", "redis://redis:6379/0")
    WTF_CSRF_ENABLED = False
    TESTING = False
    DEBUG = False


class DevelopmentConfig(BaseConfig):
    """Development configuration."""

    DEBUG = True


class TestingConfig(BaseConfig):
    """Testing configuration."""

    TESTING = True


class ProductionConfig(BaseConfig):
    """Production configuration."""

    WTF_CSRF_ENABLED = True


class CeleryConfig(object):
    """Celery configuration."""

    CELERY_BROKER_URL = os.getenv("CELERY_BROKER", "redis://redis_train:6379/0")
    CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND", "redis://redis_train:6379/0")

class CeleryHeadquarterConfig(object):
    """Celery Headquarter Config"""

    CELERY_BROKER_URL = os.getenv("CELERY_HEADQUARTER_BROKER", "redis://redis_headquarter:6379/0")
    CELERY_RESULT_BACKEND = os.getenv("CELERY_HEADQUARTER_RESULT_BACKEND", "redis://redis_headquarter:6379/0")

