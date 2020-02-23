import unittest
from unittest import TestCase
from unittest.mock import Mock, call, patch

from train.app.beat import celery_headquarter, train_speed, train_station


class TestCeleryPeriodicTasks(TestCase):
    def test_train_speed(self):
        # arrange
        celery_headquarter.send_task = Mock()
        self.expected_speed = 99.05

        # act
        with patch("train.app.beat.get_train_speed", return_value=self.expected_speed):
            train_speed()

        # assert
        celery_headquarter.send_task.assert_called_once()

        self.__check_if_proper_task_with_train_speed_has_been_send_to_celery_headquarter(
            celery_headquarter.send_task.call_args_list[0]
        )

    def __check_if_proper_task_with_train_speed_has_been_send_to_celery_headquarter(
        self, call_args
    ):
        self.assertEqual(2, len(call_args))
        expected = call(
            "periodic.train_speed", ({"actual_speed": self.expected_speed},)
        )
        self.assertEqual(expected, call_args)

    def test_train_station(self):
        # arrange
        celery_headquarter.send_task = Mock()
        self.expected_station = "Test"

        # act
        with patch(
            "train.app.beat.get_train_station", return_value=self.expected_station
        ):
            train_station()

        # assert
        celery_headquarter.send_task.assert_called_once()

        self.__check_if_proper_task_with_train_station_has_been_send_to_celery_headquarter(
            celery_headquarter.send_task.call_args_list[0]
        )

    def __check_if_proper_task_with_train_station_has_been_send_to_celery_headquarter(
        self, call_args
    ):
        self.assertEqual(2, len(call_args))
        expected = call(
            "periodic.train_station", ({"train_station": self.expected_station},)
        )
        self.assertEqual(expected, call_args)


if __name__ == "__main__":
    unittest.main()
