import unittest

from flask import current_app
from flask_testing import TestCase

from train.app.rest import create_app
from train.domain import APP_SETTINGS
from train.domain.config import CeleryConfig, CeleryHeadquarterConfig

app = create_app()


class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object(APP_SETTINGS["Development"])
        return app

    def test_app_is_development(self):
        self.assertEqual("train", current_app.config["APP_NAME"])
        self.assertEqual("redis://redis:6379/0", current_app.config["REDIS_URL"])
        self.assertFalse(current_app.config["WTF_CSRF_ENABLED"])
        self.assertFalse(current_app.config["TESTING"])
        self.assertTrue(current_app.config["DEBUG"])
        self.assertFalse(current_app is None)


class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object(APP_SETTINGS["Test"])
        return app

    def test_app_is_testing(self):
        self.assertEqual("train", current_app.config["APP_NAME"])
        self.assertEqual("redis://redis:6379/0", current_app.config["REDIS_URL"])
        self.assertFalse(current_app.config["WTF_CSRF_ENABLED"])
        self.assertTrue(current_app.config["TESTING"])
        self.assertFalse(current_app.config["DEBUG"])
        self.assertFalse(current_app is None)


class TestProductionConfig(TestCase):
    def create_app(self):
        app.config.from_object(APP_SETTINGS["Production"])
        return app

    def test_app_is_production(self):
        self.assertEqual("train", current_app.config["APP_NAME"])
        self.assertEqual("redis://redis:6379/0", current_app.config["REDIS_URL"])
        self.assertTrue(current_app.config["WTF_CSRF_ENABLED"])
        self.assertFalse(current_app.config["TESTING"])
        self.assertFalse(current_app.config["DEBUG"])
        self.assertFalse(current_app is None)


class TestCeleryConfig(unittest.TestCase):
    def test_beat_celery_config(self):
        self.assertEqual("redis://redis_train:6379/0", CeleryConfig.CELERY_BROKER_URL)
        self.assertEqual(
            "redis://redis_train:6379/0", CeleryConfig.CELERY_RESULT_BACKEND
        )


class TestCeleryHeadquarterConfig(unittest.TestCase):
    def test_celery_headquarter_config(self):
        self.assertEqual(
            "redis://redis_headquarter:6379/0",
            CeleryHeadquarterConfig.CELERY_BROKER_URL,
        )
        self.assertEqual(
            "redis://redis_headquarter:6379/0",
            CeleryHeadquarterConfig.CELERY_RESULT_BACKEND,
        )


if __name__ == "__main__":
    unittest.main()
