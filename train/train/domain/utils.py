import random

MINIMAL_SPEED = 0
MAX_SPEED = 180
DECIMAL_PLACES = 1

STATIONS = (
    "Wałcz",
    "Ostrowiec Wałecki",
    "Wiesiołka",
    "Zabrodzie",
    "Płytnica",
    "Łowisko",
    "Tarnówka",
    "Węgierce",
    "Annopole",
    "Klukowo",
    "Złotów",
    "Mogilno",
    "Sucharzewo",
    "Mokre",
    "Sławno",
    "Radosław Sławieński",
    "Staniewice",
    "Postomino",
    "Złakowo",
    "Duninowo",
)


def get_train_speed():
    MULTI = 10 * DECIMAL_PLACES
    return random.randint(MINIMAL_SPEED, MAX_SPEED * MULTI) / MULTI


def get_train_station():
    return random.choice(STATIONS)
