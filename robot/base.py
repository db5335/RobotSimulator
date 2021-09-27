import math

import pygame

from robot.color_sensor import ColorSensor
from robot.touch_sensor import TouchSensor


class Base(pygame.sprite.Sprite):
    '''
    The Base class is a pygame Sprite which represents the base of the robot.
    '''

    def __init__(self, x, y):
        '''
        Initialize the robot base.

        :param x: starting x coordinate
        :param y: starting y coordinate
        '''
        super(Base, self).__init__()
        self.width = 150
        self.update_offset()

        self.components = [None] * 16

        self.surf = pygame.Surface((self.width, self.width), pygame.SRCALPHA)
        self.update_surf()
        self.x = x - self.offset
        self.y = y - self.offset

        self.center_x = self.x + self.width / 2
        self.center_y = self.y + self.width / 2
        self.direction = 0

    def set_grid(self, grid):
        '''
        Set the grid that the robot is on.

        :param grid: the grid
        :return: None
        '''
        self.grid = grid

    def set_background(self, background):
        '''
        Set the background that the robot is on.

        :param background: the robot's background
        :return: None
        '''
        self.background = background

    def update_offset(self):
        '''
        Update the offset from the edge of the robot to its center.

        :return: None
        '''
        self.offset = (self.width - 100) / 2

    def update_surf(self):
        '''
        Update the visual representation of the robot.

        :return: None
        '''
        base = pygame.Surface((100, 100))
        base.fill((200, 200, 200))

        front = pygame.Surface((20, 20))
        front.fill((255, 0, 0))

        self.surf.blit(base, (self.offset, self.offset))
        self.surf.blit(front, (self.offset + 80, self.offset + 40))

        self.surf_copy = self.surf

    def add_component(self, component, port):
        '''
        Add a component to the robot.

        :param component: the component to add
        :param port: the component's port
        :return: None
        '''
        self.components[port - 1] = component

        if port >= 1 and port <= 4:
            start_x = 100 + self.offset
            start_y = self.offset + (port - 1) * 25
        elif port >= 5 and port <= 8:
            start_x = self.offset + 100 - (port - 4) * 25
            start_y = 100 + self.offset
        elif port >= 9 and port <= 12:
            start_x = 0
            start_y = self.offset + 100 - (port - 8) * 25
        elif port >= 13 and port <= 16:
            start_x = self.offset + (port - 13) * 25
            start_y = 0

        if component is None:
            pygame.draw.rect(self.surf, (0, 0, 0, 0), (start_x, start_y, 25, 25))
        else:
            if port >= 1 and port <= 4:
                component.set_pos(62.5 + self.center_x, (port - 2.5) * 25 + self.center_y, self.direction)
            elif port >= 5 and port <= 8:
                component.set_pos(self.center_x - (port - 6.5) * 25, 62.5 + self.center_y, self.direction)
            elif port >= 9 and port <= 12:
                component.set_pos(self.center_x - 62.5, self.center_y - (port - 10.5) * 25, self.direction)
            elif port >= 13 and port <= 16:
                component.set_pos(self.center_x + (port - 14.5) * 25, self.center_y - 62.5, self.direction)
            self.surf.blit(component.surf, (start_x, start_y))

    def get_component_by_port(self, port):
        '''
        Get the component at the given port.

        :param port: the port of the component
        :return: the component
        '''
        return self.components[port - 1]

    def reset_pos(self):
        '''
        Reset the x and y coordinates of the robot.

        :return: None
        '''
        self.y = self.center_y - self.width * (math.fabs(math.cos(math.radians(self.direction)))
                                               + math.fabs(math.sin(math.radians(self.direction)))) / 2
        self.x = self.center_x - self.width * (math.fabs(math.cos(math.radians(self.direction)))
                                               + math.fabs(math.sin(math.radians(self.direction)))) / 2

    def move_forward(self, speed):
        '''
        Move forward at the given speed.

        :param speed: the speed at which to move
        :return: None
        '''
        self.center_y -= speed / 10 * math.sin(math.radians(self.direction))
        self.center_x += speed / 10 * math.cos(math.radians(self.direction))
        self.reset_pos()
        for component in self.components:
            if component is not None:
                component.move_forward(speed)

    def move_backward(self, speed):
        '''
        Move backward at the given speed.

        :param speed: the speed at which to move
        :return: None
        '''
        self.move_forward(-1 * speed)

    def turn_cw(self, speed):
        '''
        Turn clockwise at the given speed.

        :param speed: the speed at which to turn
        :return: None
        '''
        self.direction -= speed / 10
        self.surf = pygame.transform.rotate(self.surf_copy, self.direction)
        self.reset_pos()
        for component in self.components:
            if component is not None:
                component.turn_cw(speed, self)

    def turn_counter_cw(self, speed):
        '''
        Move counterclockwise at the given speed.

        :param speed: the speed at which to turn
        :return: None
        '''
        self.turn_cw(-1 * speed)

    def save(self, file_name):
        '''
        Save the robot in a file.

        :param file_name: the file to save it in
        :return: None
        '''
        with open(file_name, 'w') as file:
            for i in range(0, 16):
                if self.components[i] is not None:
                    file.write(str(i + 1) + "," + str(self.components[i]) + '\n')

    def init_from_file(self, file_name):
        '''
        Initialize a robot from a saved file.

        :param file_name: the file in which the robot is saved
        :return: None
        '''
        with open(file_name) as file:
            for line in file:
                fields = line.split(',')
                port = int(fields[0])
                sensor = fields[1][:-1]
                if sensor == 'Touch Sensor':
                    self.add_component(TouchSensor(self), port)
                elif sensor == 'Color Sensor':
                    self.add_component(ColorSensor(self), port)
                # TODO add ultrasound sensor
