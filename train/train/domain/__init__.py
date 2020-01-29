import os

from celery import Celery
from flask import Flask

from train.domain.config import CeleryConfig

APP_SETTINGS = {
    "Development": "train.domain.config.DevelopmentConfig",
    "Test": "train.domain.config.TestingConfig",
    "Production": "train.domain.config.ProductionConfig",
}


def create_app():

    # instantiate the app
    app = Flask(__name__)

    # set config
    app_settings = os.getenv("APP_SETTINGS", "BaseConfig")
    app.config.from_object(APP_SETTINGS[app_settings])

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {"app": app}

    return app


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
