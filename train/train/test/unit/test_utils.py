from train.domain.utils import (
    MAX_SPEED,
    MINIMAL_SPEED,
    STATIONS,
    get_train_speed,
    get_train_station,
)


def test_get_train_speed():
    train_speed = get_train_speed()
    assert MINIMAL_SPEED <= train_speed <= MAX_SPEED


def test_get_train_station():
    train_station = get_train_station()
    assert train_station in STATIONS
