import pygame

from code.condition import Condition
from code.conditions import *


class ColorCondition(Condition):
    def __init__(self, condition, target, color, min, max):
        super().__init__(condition)
        self.target = target
        if self.condition == ColorConditions.EXACT:
            self.color = color
        elif self.condition == ColorConditions.RANGE:
            self.min = min
            self.max = max

    def is_met(self):
        if self.condition == ColorConditions.EXACT:
            if self.target.check_color(self.color):
                return True
        elif self.condition == ColorConditions.RANGE:
            if self.target.check_color_range(self.min, self.max):
                return True
        return False
