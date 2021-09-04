from time import time, sleep

import pygame

from code.directions import TurnDirection


class TurnBlock:
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
            if self.direction == TurnDirection.COUNTER_CLOCKWISE:
                self.target.turn_counter_cw(self.speed)
            else:
                self.target.turn_cw(self.speed)
            self.display.blit(self.target.background, (0, 0))
            self.display.blit(self.target.surf, (self.target.x, self.target.y))
            py_clock.tick(100)
            pygame.display.update()
