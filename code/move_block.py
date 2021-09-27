from time import time

import pygame

from code.directions import MoveDirection


class MoveBlock:
    '''
    Class for a move action block.
    '''

    def __init__(self, display, target, direction, speed, duration):
        '''
        Create a new move block.

        :param display: the display to update
        :param target: the robot to move
        :param direction: the direction to move
        :param speed: the speed at which to move
        :param duration: the time for which to move
        '''
        self.display = display
        self.target = target

        self.direction = direction
        self.speed = speed
        self.duration = duration

    def execute(self):
        '''
        Move for the given duration at the given speed and direction.

        :return: None
        '''
        py_clock = pygame.time.Clock()

        start = time()
        while (time() - start < self.duration):
            if self.direction == MoveDirection.FORWARD:
                self.target.move_forward(self.speed)
            else:
                self.target.move_backward(self.speed)
            self.display.blit(self.target.background, (0, 0))
            self.display.blit(self.target.surf, (self.target.x, self.target.y))
            py_clock.tick(100)
            pygame.display.update()
