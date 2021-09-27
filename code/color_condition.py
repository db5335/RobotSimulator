from code.condition import Condition
from code.conditions import *


class ColorCondition(Condition):
    '''
    Class for checking color conditions.
    '''

    def __init__(self, condition, target, color, min, max):
        '''
        Initialize the condition.

        :param condition: the type of condition
        :param target: the sensor
        :param color: the color to check for
        :param min: the min color in the range
        :param max: the max color in the range
        '''
        super().__init__(condition)
        self.target = target
        if self.condition == ColorConditions.EXACT:
            self.color = color
        elif self.condition == ColorConditions.RANGE:
            self.min = min
            self.max = max

    def is_met(self):
        '''
        Check if the condition is met.

        :return: the truth value of the condition
        '''
        if self.condition == ColorConditions.EXACT:
            if self.target.check_color(self.color):
                return True
        elif self.condition == ColorConditions.RANGE:
            if self.target.check_color_range(self.min, self.max):
                return True
        return False
