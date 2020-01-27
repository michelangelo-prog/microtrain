import os

from flask import Flask

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
