from code.condition import Condition
from code.conditions import *


class UltrasoundCondition(Condition):
    '''
    Class for checking ultrasound conditions.
    '''
    def __init__(self, condition, target, distance):
        '''
        Initialize the condition.

        :param condition: the type of condition
        :param target: the sensor
        :param distance: the distance to compare to
        '''
        super().__init__(condition)
        self.target = target
        self.distance = distance

    def is_met(self):
        '''
        Check if the condition is met.

        :return: the truth value of the condition
        '''
        if self.condition == UltrasoundConditions.LESS_THAN:
            return self.target.get_distance() < self.distance
        elif self.condition == UltrasoundConditions.GREATER_THAN:
            return self.target.get_distance() > self.distance
        return False