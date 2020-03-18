import datetime
import os
from unittest import TestCase
from unittest.mock import Mock, call, mock_open, patch

from headquarter.domain import LOG_DIR
from headquarter.domain.handlers.speed_handler import (
    FILE_NAMES,
    SpeedHandler,
    speed_ranges,
)

CURRENT_TIME = datetime.datetime(2010, 10, 10)


class TestSpeedHandler(TestCase):
    def test_save_min_slow_speed_to_slow_log(self):
        speed = speed_ranges["slow"]["MIN"]
        expected_log_file_path = os.path.join(LOG_DIR, FILE_NAMES["slow"])
        with patch(
            "headquarter.domain.handlers.speed_handler.datetime",
            Mock(now=Mock(return_value=CURRENT_TIME)),
        ):
            self.__check_if_speed_will_be_save_properly(speed, expected_log_file_path)

    def test_save_max_slow_speed_to_slow_log(self):
        speed = speed_ranges["slow"]["MAX"]
        expected_log_file_path = os.path.join(LOG_DIR, FILE_NAMES["slow"])
        with patch(
            "headquarter.domain.handlers.speed_handler.datetime",
            Mock(now=Mock(return_value=CURRENT_TIME)),
        ):
            self.__check_if_speed_will_be_save_properly(speed, expected_log_file_path)

    def test_slow_speed_to_slow_log(self):
        speed = 22.1
        expected_log_file_path = os.path.join(LOG_DIR, FILE_NAMES["slow"])
        with patch(
            "headquarter.domain.handlers.speed_handler.datetime",
            Mock(now=Mock(return_value=CURRENT_TIME)),
        ):
            self.__check_if_speed_will_be_save_properly(speed, expected_log_file_path)

    def test_save_min_normal_speed_to_normal_log(self):
        speed = speed_ranges["normal"]["MIN"]
        expected_log_file_path = os.path.join(LOG_DIR, FILE_NAMES["normal"])
        with patch(
            "headquarter.domain.handlers.speed_handler.datetime",
            Mock(now=Mock(return_value=CURRENT_TIME)),
        ):
            self.__check_if_speed_will_be_save_properly(speed, expected_log_file_path)

    def test_save_max_normal_speed_to_normal_log(self):
        speed = speed_ranges["normal"]["MAX"]
        expected_log_file_path = os.path.join(LOG_DIR, FILE_NAMES["normal"])
        with patch(
            "headquarter.domain.handlers.speed_handler.datetime",
            Mock(now=Mock(return_value=CURRENT_TIME)),
        ):
            self.__check_if_speed_will_be_save_properly(speed, expected_log_file_path)

    def test_normal_speed_to_normal_log(self):
        speed = 111.1
        expected_log_file_path = os.path.join(LOG_DIR, FILE_NAMES["normal"])
        with patch(
            "headquarter.domain.handlers.speed_handler.datetime",
            Mock(now=Mock(return_value=CURRENT_TIME)),
        ):
            self.__check_if_speed_will_be_save_properly(speed, expected_log_file_path)

    def test_save_min_fast_speed_to_fast_log(self):
        speed = speed_ranges["fast"]["MIN"]
        expected_log_file_path = os.path.join(LOG_DIR, FILE_NAMES["fast"])
        with patch(
            "headquarter.domain.handlers.speed_handler.datetime",
            Mock(now=Mock(return_value=CURRENT_TIME)),
        ):
            self.__check_if_speed_will_be_save_properly(speed, expected_log_file_path)

    def test_save_max_fast_speed_to_fast_log(self):
        speed = speed_ranges["fast"]["MAX"]
        expected_log_file_path = os.path.join(LOG_DIR, FILE_NAMES["fast"])
        with patch(
            "headquarter.domain.handlers.speed_handler.datetime",
            Mock(now=Mock(return_value=CURRENT_TIME)),
        ):
            self.__check_if_speed_will_be_save_properly(speed, expected_log_file_path)

    def test_fast_speed_to_fast_log(self):
        speed = 155.5
        expected_log_file_path = os.path.join(LOG_DIR, FILE_NAMES["fast"])
        with patch(
            "headquarter.domain.handlers.speed_handler.datetime",
            Mock(now=Mock(return_value=CURRENT_TIME)),
        ):
            self.__check_if_speed_will_be_save_properly(speed, expected_log_file_path)

    def __check_if_speed_will_be_save_properly(self, speed, expected_file_path):
        speed_handler = SpeedHandler()

        mock_file = mock_open()
        with patch("headquarter.domain.handlers.speed_handler.open", mock_file):
            speed_handler.save_speed(speed)

        expected_open_call = call(expected_file_path, "a")
        expected_text_in_write_call = "time: {}  speed: {} \n".format(
            CURRENT_TIME, speed
        )
        expected_write_call = call().write(expected_text_in_write_call)
        expected_close_call = call().close()

        self.assertEqual(expected_open_call, mock_file.mock_calls[0])
        self.assertEqual(expected_write_call, mock_file.mock_calls[1])
        self.assertEqual(expected_close_call, mock_file.mock_calls[2])
