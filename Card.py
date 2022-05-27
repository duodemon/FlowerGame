from enum import *


class Card:
    def __init__(self, value, color, id):
        self.value = value
        self.color = color
        self.id = id

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __eq__(self, other):
        return self.value == other.value

    def __str__(self):
        return self.id.name


class Color(Enum):
    BLACK = 0,
    RED = 1,
    MIXED = 2


class Name(Enum):
    RED_EYE = 0,
    OPERETTA = 1,
    BLACK_EYE = 2,
    OBLIQUE = 3,
    OPERA = 4,
    SIX = 5,
    SEVEN = 6,
    RED_EIGHT = 7,
    LITTLE_BULL = 8,
    BIG_BULL = 9,
    BLACK_TEN = 10,
    FLOWERED_TEN = 11,
    TIGER = 12,
    GOD = 13

