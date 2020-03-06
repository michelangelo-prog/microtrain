from datetime import datetime
import os

from headquarter.domain import LOG_DIR

from headquarter.domain.adapters.gatekeeper_adapter import GatekeeperAdapter

from multiprocessing import Process

LOG_FILE_NAME = "info.log"
import time

CLOSE_BARRIER_TIME_IN_SEC = 10

class StationHandler:
    def __init__(self):
        self.info_log_path = os.path.join(LOG_DIR, LOG_FILE_NAME)
        self.gatekeeper_adapter = GatekeeperAdapter()

    def train_goes_to_station(self, station_name):
        self.__save_station_to_info_log(station_name)
        self.__check_barrier_status(station_name)
        self.__open_barrier_after_time(station_name, CLOSE_BARRIER_TIME_IN_SEC)

    def __check_barrier_status(self, station_name):
        if self.__check_if_station_barrier_is_open(station_name):
            self.close_barrier(station_name)
        else:
            self.__save_error_to_info_log(station_name, "barrier closed")

    def __check_if_station_barrier_is_open(self, station_name):
        response_json = self.gatekeeper_adapter.get_station_barrier_status(station_name)
        return True if response_json["status"] == "open" else False

    def close_barrier(self, station_name):
        self.gatekeeper_adapter.set_station_barrier_status(station_name, "closed")

    def __save_error_to_info_log(self, station_name, error_info):
        text = "time: {}  station_name: {} error_info: {} \n".format(datetime.now(), station_name, error_info)
        self.__append_text_to_info_log_file(text)


    def __save_station_to_info_log(self, station_name):
        text = "time: {}  station_name: {} \n".format(datetime.now(), station_name)
        self.__append_text_to_info_log_file(text)

    def __append_text_to_info_log_file(self, text):
        file = open(self.info_log_path, "a")
        file.write(text)
        file.close()

    def __start_process_to_open_barrier_after_time(self, station_name, sec):
        time.sleep(sec)
        self.open_barrier(station_name)
        self.__save_opening_time_into_log(station_name)

    def open_barrier(self, station_name):
        self.gatekeeper_adapter.set_station_barrier_status(station_name, "open")

    def __save_opening_time_into_log(self, station_name):
        text = "time: {}  station_name: {} status: barrier opened \n".format(datetime.now(), station_name)
        self.__append_text_to_info_log_file(text)

    def __open_barrier_after_time(self, station_name, sec):
        p = Process(target=self.__start_process_to_open_barrier_after_time, args=(station_name, sec))
        p.start()
        p.join()
