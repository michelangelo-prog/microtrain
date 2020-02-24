import unittest

import pytest

from gatekeeper.tests.component.mixins import BaseTestCase


class TestBarrierBlueprint(BaseTestCase):
    @pytest.mark.skip(reason="TODO")
    def test_get_actual_barrier_status_when_barrier_is_open(self):
        pass

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
