import os

APP_DIR = os.getcwd()

LOG_DIR = os.path.join(APP_DIR, "headquarter/logs/")

APP_SETTINGS = {
    "Development": "headquarter.domain.config.DevelopmentConfig",
    "Test": "headquarter.domain.config.TestingConfig",
    "Production": "headquarter.domain.config.ProductionConfig",
}
