from unittest import TestCase, mock
from unittest.mock import call

from requests.exceptions import RequestException

from headquarter.domain.adapters.gatekeeper_adapter import (
    GatekeeperAdapter,
    GatekeeperAdapterResponseException,
)


def mocked_requests_get(*args, **kwargs):
    url = kwargs.get("url")
    params = kwargs.get("params")

    if url == "http://gatekeeper:5000/api/v1/barrier" and params == {"station": "Test"}:
        return MockResponse({"status": "open"}, 200)

    return MockResponse({"error": "Not found"}, 404)


class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data


class TestGatekeeperAdapter(TestCase):
    @mock.patch(
        "headquarter.domain.adapters.gatekeeper_adapter.requests.get",
        side_effect=mocked_requests_get,
    )
    def test_get_station_barrier_status(self, mock_get):
        adapter = GatekeeperAdapter()
        station_name = "Test"
        status = adapter.get_station_barrier_status(station_name)

        expected_status = {"status": "open"}
        expected_call = call(
            params={"station": station_name},
            url="http://gatekeeper:5000/api/v1/barrier",
        )

        self.assertEqual(expected_status, status)
        mock_get.assert_called_once()
        self.assertIn(expected_call, mock_get.call_args_list)

    @mock.patch(
        "headquarter.domain.adapters.gatekeeper_adapter.requests.get",
        side_effect=mocked_requests_get,
    )
    def test_raise_exception_when_get_barrier_status_and_status_code_is_different_then_200(
        self, mock_get
    ):
        adapter = GatekeeperAdapter()
        station_name = "Test_2"

        with self.assertRaises(GatekeeperAdapterResponseException) as error:
            adapter.get_station_barrier_status(station_name)

        expected_exception_msg = "Invalid response: 404, {'error': 'Not found'}"
        expected_call = call(
            params={"station": station_name},
            url="http://gatekeeper:5000/api/v1/barrier",
        )

        self.assertEqual(expected_exception_msg, str(error.exception))
        mock_get.assert_called_once()
        self.assertIn(expected_call, mock_get.call_args_list)

    @mock.patch(
        "headquarter.domain.adapters.gatekeeper_adapter.requests.get",
        side_effect=RequestException("test"),
    )
    def test_raise_exception_when_get_barrier_status_and_request_raise_request_exception(
        self, mock_get
    ):
        adapter = GatekeeperAdapter()
        station_name = "Test"

        with self.assertRaises(GatekeeperAdapterResponseException) as error:
            adapter.get_station_barrier_status(station_name)

        expected_exception_msg = "Invalid request GET: test"
        expected_call = call(
            params={"station": station_name},
            url="http://gatekeeper:5000/api/v1/barrier",
        )

        self.assertEqual(expected_exception_msg, str(error.exception))
        mock_get.assert_called_once()
        self.assertIn(expected_call, mock_get.call_args_list)