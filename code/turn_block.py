from time import time

import pygame

from code.directions import TurnDirection


class TurnBlock:
    '''
    Class for a turn action block.
    '''

    def __init__(self, display, target, direction, speed, duration):
        '''
        Create a new turn block.

        :param display: the display to update
        :param target: the robot to turn
        :param direction: the direction to turn
        :param speed: the speed at which to turn
        :param duration: the time for which to turn
        '''
        self.display = display
        self.target = target

        self.direction = direction
        self.speed = speed
        self.duration = duration

    def execute(self):
        '''
        Turn for the given duration at the given speed and direction.

        :return: None
        '''
        py_clock = pygame.time.Clock()

        start = time()
        while (time() - start < self.duration):
            if self.direction == TurnDirection.COUNTER_CLOCKWISE:
                self.target.turn_counter_cw(self.speed)
            else:
                self.target.turn_cw(self.speed)
            self.display.blit(self.target.background, (0, 0))
            self.display.blit(self.target.surf, (self.target.x, self.target.y))
            py_clock.tick(100)
            pygame.display.update()
