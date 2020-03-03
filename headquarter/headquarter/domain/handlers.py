import os
from datetime import datetime

from headquarter.domain import APP_DIR

LOG_DIR = "{}/headquarter/logs/".format(APP_DIR)

FILE_NAMES = {"slow": "slow.log", "normal": "normal.log", "fast": "fast.log"}

speed_ranges = {
    "slow": {"MIN": 0.0, "MAX": 40.0},
    "normal": {"MIN": 40.1, "MAX": 140.0},
    "fast": {"MIN": 140.1, "MAX": 180.0},
}


class SpeedHandler:
    def save_speed(self, speed):
        file_name = self.__get_file_name(speed)
        current_time = self.__get_current_time()
        self.__save_speed_to_file(file_name, speed, current_time)

    def __get_file_name(self, speed):
        if speed_ranges["slow"]["MIN"] <= speed <= speed_ranges["slow"]["MAX"]:
            return FILE_NAMES["slow"]
        elif speed_ranges["normal"]["MIN"] <= speed <= speed_ranges["normal"]["MAX"]:
            return FILE_NAMES["normal"]
        elif speed_ranges["fast"]["MIN"] <= speed <= speed_ranges["fast"]["MAX"]:
            return FILE_NAMES["fast"]

    def __save_speed_to_file(self, file_name, speed, time):
        path = os.path.join(LOG_DIR, file_name)
        file = open(path, "a")
        file.write("time: {}  speed: {} \n".format(time, speed))
        file.close()

    def __get_current_time(self):
        return datetime.now()
