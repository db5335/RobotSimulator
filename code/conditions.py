from enum import Enum

class TouchConditions(Enum):
    '''
    Enum for touch conditions.
    '''
    TOUCHED = 1
    RELEASED = 2

class ColorConditions(Enum):
    '''
    Enum for color conditions.
    '''
    EXACT = 1
    RANGE = 2

class UltrasoundConditions(Enum):
    '''
    Enum for ultrasound conditions.
    '''
    LESS_THAN = 1
    GREATER_THAN = 2
