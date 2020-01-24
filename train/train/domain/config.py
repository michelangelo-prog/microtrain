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
