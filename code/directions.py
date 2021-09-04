from enum import Enum


class MoveDirection(Enum):
    FORWARD = True
    BACKWARD = False

class TurnDirection(Enum):
    COUNTER_CLOCKWISE = True
    CLOCKWISE = False