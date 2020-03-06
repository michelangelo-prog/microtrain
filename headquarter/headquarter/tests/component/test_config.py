import unittest

from flask import current_app
from flask_testing import TestCase

from headquarter.app.rest import create_app
from headquarter.domain import APP_SETTINGS

app = create_app()


class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object(APP_SETTINGS["Development"])
        return app

    def test_app_is_development(self):
        self.assertEqual("headquarter", current_app.config["APP_NAME"])
        self.assertFalse(current_app.config["WTF_CSRF_ENABLED"])
        self.assertFalse(current_app.config["TESTING"])
        self.assertTrue(current_app.config["DEBUG"])
        self.assertFalse(current_app is None)


class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object(APP_SETTINGS["Test"])
        return app

    def test_app_is_testing(self):
        self.assertEqual("headquarter", current_app.config["APP_NAME"])
        self.assertFalse(current_app.config["WTF_CSRF_ENABLED"])
        self.assertTrue(current_app.config["TESTING"])
        self.assertFalse(current_app.config["DEBUG"])
        self.assertFalse(current_app is None)


class TestProductionConfig(TestCase):
    def create_app(self):
        app.config.from_object(APP_SETTINGS["Production"])
        return app

    def test_app_is_production(self):
        self.assertEqual("headquarter", current_app.config["APP_NAME"])
        self.assertTrue(current_app.config["WTF_CSRF_ENABLED"])
        self.assertFalse(current_app.config["TESTING"])
        self.assertFalse(current_app.config["DEBUG"])
        self.assertFalse(current_app is None)


if __name__ == "__main__":
    unittest.main()
