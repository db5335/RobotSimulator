from enum import Enum

class TouchConditions(Enum):
    TOUCHED = 1
    RELEASED = 2

class ColorConditions(Enum):
    EXACT = 1
    RANGE = 2
