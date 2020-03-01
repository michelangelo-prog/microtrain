import unittest

from gatekeeper.domain import db
from gatekeeper.tests.component.mixins import BarrierMixin, BaseTestCase
from gatekeeper.tests.factories import StationFactory


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
        expected_json = {"status": status}
        self.assertEqual(expected_json, response.json)

    def test_get_actual_barrier_status_when_barrier_is_closed(self):
        self.station = self.__given_station_with_closed_barrier()
        self.response = self.__when_client_checks_status_of_barrier_at_the_station(
            self.station.name
        )
        self.__then_client_receives_information_that_barrier_has_expected_status(
            response=self.response, status="closed"
        )

    def __given_station_with_closed_barrier(self):
        station = self.__create_station_object()
        station.barrier.is_open = False
        self.__add_object_to_db(station)
        return station

    def test_return_404_when_barrier_does_not_exist(self):
        self.__given_station_with_closed_barrier()
        self.response = self.__when_client_checks_status_of_barrier_at_the_station(
            "TEST"
        )
        self.__then_client_get_400(self.response)

    def __then_client_get_400(self, response):
        self.assertEqual(400, response.status_code)

    def test_barrier_is_closed_by_client(self):
        self.station = self.__given_station_with_open_barrier()
        self.response = self.__when_client_requests_to_change_barrier_status(
            station_name=self.station.name, barrier_status="closed"
        )
        self.__then_client_get_201_with_status(self.response, "success")

    def __when_client_requests_to_change_barrier_status(
        self, station_name, barrier_status
    ):
        json = {"station": station_name, "barrier_status": barrier_status}
        return self.change_barrier_status(json=json)

    def __then_client_get_201_with_status(self, response, expected_status):
        self.assertEqual(201, response.status_code)
        expected_json = {"status": expected_status}
        self.assertEqual(expected_json, response.json)

    def test_barrier_is_opened_by_client(self):
        self.station = self.__given_station_with_closed_barrier()
        self.response = self.__when_client_requests_to_change_barrier_status(
            station_name=self.station.name, barrier_status="open"
        )
        self.__then_client_get_201_with_status(self.response, "success")

    def test_barrier_stay_closed_when_client_want_to_close_barrier(self):
        self.station = self.__given_station_with_closed_barrier()
        self.response = self.__when_client_requests_to_change_barrier_status(
            station_name=self.station.name, barrier_status="closed"
        )
        self.__then_client_get_201_with_status(self.response, "success")

    def test_barrier_stay_open_when_client_want_to_open_barrier(self):
        self.station = self.__given_station_with_open_barrier()
        self.response = self.__when_client_requests_to_change_barrier_status(
            station_name=self.station.name, barrier_status="open"
        )
        self.__then_client_get_201_with_status(self.response, "success")

    def test_return_400_when_client_want_to_close_not_existing_barrier(self):
        self.__given_station_with_closed_barrier()
        self.response = self.__when_client_requests_to_change_barrier_status(
            station_name="TEST", barrier_status="closed"
        )
        self.__then_client_get_400_with_status(self.response, "fail")

    def __then_client_get_400_with_status(self, response, status):
        self.assertEqual(400, response.status_code)
        expected_json = {"status": "fail"}
        self.assertEqual(expected_json, response.json)

    def test_return_400_when_client_want_to_open_not_existing_barrier(self):
        self.__given_station_with_closed_barrier()
        self.response = self.__when_client_requests_to_change_barrier_status(
            station_name="TEST", barrier_status="open"
        )
        self.__then_client_get_400_with_status(self.response, "fail")


if __name__ == "__main__":
    unittest.main()
