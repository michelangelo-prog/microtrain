import os

import requests


class GatekeeperAdapterResponseException(Exception):
    """Raise exception when invalid response"""

    pass


class GatekeeperAdapter:
    def __init__(self):
        self.gatekeeper_endpoint = os.getenv(
            "GATEKEEPER_ENDPOINT", "http://gatekeeper:5000/api/v1/barrier"
        )

    def get_station_barrier_status(self, station_name):
        response = requests.get(
            url=self.gatekeeper_endpoint, params={"station": station_name}
        )
        response_json = response.json()
        if not response.status_code == 200:
            raise GatekeeperAdapterResponseException(
                "Invalid GET response: {}, {}".format(
                    response.status_code, response_json
                )
            )
        return response_json

    def set_station_barrier_status(self, station_name, barrier_status):
        json = {"station": station_name, "barrier_status": barrier_status}
        response = requests.post(url=self.gatekeeper_endpoint, json=json)
        response_json = response.json()
        if not response.status_code == 201:
            raise GatekeeperAdapterResponseException(
                "Invalid POST response: {}, {}".format(
                    response.status_code, response_json
                )
            )
        return response_json
