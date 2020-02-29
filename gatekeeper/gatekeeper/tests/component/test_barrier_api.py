import unittest

import pytest

from gatekeeper.tests.component.mixins import BaseTestCase, BarrierMixin
from gatekeeper.tests.factories import StationFactory

from gatekeeper.domain import db


class TestBarrierBlueprint(BarrierMixin, BaseTestCase):
    def test_get_actual_barrier_status_when_barrier_is_open(self):
        self.station = self.__given_station_with_open_barrier()
        self.response = self.__when_client_checks_status_of_barrier_at_the_station(
            self.station.name
        )
        self.__then_client_receives_information_that_barrier_has_expected_status(
            response=self.response, status="open"
        )

    def __given_station_with_open_barrier(self):
        station = self.__create_station_object()
        self.__add_object_to_db(station)
        return station

    def __create_station_object(self):
        station = StationFactory()
        return station

    def __add_object_to_db(self, object):
        db.session.add(object)
        db.session.commit()

    def __when_client_checks_status_of_barrier_at_the_station(self, station_name):
        return self.get_barrier_status(station_name=station_name)

    def __then_client_receives_information_that_barrier_has_expected_status(
        self, response, status
    ):
        self.assertEqual(200, response.status_code)
        self.assertEqual(status, response.json["STATUS"])

    @pytest.mark.skip(reason="TODO")
    def test_get_actual_barrier_status_when_barrier_is_closed(self):
        pass

    @pytest.mark.skip(reason="TODO")
    def get_return_400_when_barrier_does_not_exist(self):
        pass

    @pytest.mark.skip(reason="TODO")
    def test_barrier_is_closed_by_client(self):
        pass

    @pytest.mark.skip(reason="TODO")
    def test_barrier_is_opened_by_client(self):
        pass

    @pytest.mark.skip(reason="TODO")
    def test_barrier_stay_closed_when_client_want_to_close_barrier(self):
        pass

    @pytest.mark.skip(reason="TODO")
    def test_barrier_stay_open_when_client_want_to_open_barrier(self):
        pass

    @pytest.mark.skip(reason="TODO")
    def test_return_400_when_client_want_to_close_not_existing_barrier(self):
        pass

    @pytest.mark.skip(reason="TODO")
    def test_return_400_when_client_want_to_open_not_existing_barrier(self):
        pass


if __name__ == "__main__":
    unittest.main()
