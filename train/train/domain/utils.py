import random
import time

random.seed(time.clock())

MINIMAL_SPEED = 0
MAX_SPEED = 180
DECIMAL_PLACES = 2


def get_train_speed():

    MULTI = 10 * DECIMAL_PLACES
    return random.randint(MINIMAL_SPEED, MAX_SPEED * MULTI) / MULTI
