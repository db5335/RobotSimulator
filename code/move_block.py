from time import time, sleep

import pygame

from code.directions import MoveDirection


class MoveBlock:
    def __init__(self, display, target, direction, speed, duration):
        self.display = display
        self.target = target

        self.direction = direction
        self.speed = speed
        self.duration = duration

    def execute(self):
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
