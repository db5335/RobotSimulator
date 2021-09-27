from enum import Enum


class MoveDirection(Enum):
    '''
    Enum for moving directions.
    '''
    FORWARD = True
    BACKWARD = False

class TurnDirection(Enum):
    '''
    Enum for turning directions.
    '''
    COUNTER_CLOCKWISE = True
    CLOCKWISE = False