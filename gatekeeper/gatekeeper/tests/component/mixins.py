from flask_testing import TestCase

from gatekeeper.domain import APP_SETTINGS, create_app, db


class BaseTestCase(TestCase):
    def create_app(self):
        app = create_app()
        app.config.from_object(APP_SETTINGS["Test"])
        return app

    def setUp(self):
        db.drop_all()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class BarrierMixin:
    def get_barrier_status(self, station_name):
        uri = "/api/v1/barrier"

        if station_name:
            uri += "?station={}".format(station_name)

        return self.client.get(uri)

    def change_barrier_status(self, **kwargs):
        uri = "/api/v1/barrier"
        return self.client.post(uri, **kwargs)
