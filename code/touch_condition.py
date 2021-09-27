import pygame

from code.condition import Condition
from code.conditions import *


class TouchCondition(Condition):
    '''
    Class for checking touch conditions.
    '''

    def __init__(self, condition, target):
        '''
        Initialize the condition.

        :param condition: the type of condition
        :param target: the sensor
        '''
        super().__init__(condition)
        self.target = target
        self.mouse = pygame.mouse

    def setup(self):
        '''
        Set released to true if the mouse is not on it.

        :return: None
        '''
        if not self.target.check_touched(self.mouse.get_pos()):
            self.released = True

    def is_met(self):
        '''
        Check if the condition is met.

        :return: the truth value of the condition
        '''
        if self.condition == TouchConditions.TOUCHED:
            for event in pygame.event.get():
                if event == pygame.MOUSEBUTTONDOWN:
                    if self.target.check_touched(self.mouse.get_pos()):
                        return True
            if self.mouse.get_pressed()[0]:
                if self.target.check_touched(self.mouse.get_pos()):
                    return True
        elif self.condition == TouchConditions.RELEASED:
            if self.released:
                if self.target.check_touched(self.mouse.get_pos()):
                    self.released = False
                return False
            for event in pygame.event.get():
                if event == pygame.MOUSEBUTTONUP:
                    if self.target.check_touched(self.mouse.get_pos()):
                        return True
            if not self.target.check_touched(self.mouse.get_pos()):
                return True
        return False
