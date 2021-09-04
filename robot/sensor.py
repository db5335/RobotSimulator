import math

import pygame
from func.trig import *


class Sensor(pygame.sprite.Sprite):
    def __init__(self, base):
        super(Sensor, self)
        self.base = base
        self.width = 25
        self.surf = pygame.Surface((25, 25), pygame.SRCALPHA)

    def set_pos(self, x, y, direction):
        self.center_x = x
        self.center_y = y
        self.direction = direction

        self.dist = math.sqrt((self.center_x - self.base.center_x) ** 2 + (self.center_y - self.base.center_y) ** 2)
        self.angle = math.atan((self.base.center_y - self.center_y) / (self.center_x - self.base.center_x))
        if self.center_x < self.base.center_x:
            self.angle += math.pi

        self.reset_pos()

    def reset_pos(self):
        self.y = self.center_y - self.width * (cos_abs_deg(self.direction)
                                               + sin_abs_deg(self.direction)) / 2
        self.x = self.center_x - self.width * (cos_abs_deg(self.direction)
                                               + sin_abs_deg(self.direction)) / 2

    def move_forward(self, speed):
        self.center_y -= speed / 10 * math.sin(math.radians(self.direction))
        self.center_x += speed / 10 * math.cos(math.radians(self.direction))
        self.reset_pos()

    def turn_cw(self, speed, base):
        self.direction -= speed / 10

        self.center_x = base.center_x + self.dist * math.cos(math.radians(self.direction) + self.angle)
        self.center_y = base.center_y - self.dist * math.sin(math.radians(self.direction) + self.angle)

        self.reset_pos()