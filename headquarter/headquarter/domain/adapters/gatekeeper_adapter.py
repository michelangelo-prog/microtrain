import os

import requests
from requests.exceptions import RequestException


class GatekeeperAdapterResponseException(Exception):
    """Raise exception when invalid response"""

    pass


class GatekeeperAdapter:
    def __init__(self):
        self.status_code_get_station_barrier_status = 200
        self.status_code_post_set_station_barrier_status = 201
        self.gatekeeper_endpoint = os.getenv(
            "GATEKEEPER_ENDPOINT", "http://gatekeeper:5000/api/v1/barrier"
        )

    def get_station_barrier_status(self, station_name):
        response = self.__requests_get_station_status(station_name)
        self.__check_if_response_has_required_response_status_code(
            response, self.status_code_get_station_barrier_status
        )
        return response.json()

    def __requests_get_station_status(self, station_name):
        try:
            response = requests.get(
                url=self.gatekeeper_endpoint, params={"station": station_name}
            )
            return response
        except RequestException as error:
            raise GatekeeperAdapterResponseException(
                "Invalid request GET: {}".format(error)
            )

    def __check_if_response_has_required_response_status_code(
        self, response, required_status_code
    ):
        if not response.status_code == required_status_code:
            raise GatekeeperAdapterResponseException(
                "Invalid response: {}, {}".format(response.status_code, response.json())
            )

    def set_station_barrier_status(self, station_name, barrier_status):
        json_data = {"station": station_name, "barrier_status": barrier_status}
        response = self.__requests_post_set_station_barrier_status(json_data)
        self.__check_if_response_has_required_response_status_code(
            response, self.status_code_post_set_station_barrier_status
        )
        return response.json()

    def __requests_post_set_station_barrier_status(self, json):
        try:
            response = requests.post(url=self.gatekeeper_endpoint, json=json)
            return response
        except RequestException as error:
            raise GatekeeperAdapterResponseException(
                "Invalid request POST: {}".format(error)
            )
