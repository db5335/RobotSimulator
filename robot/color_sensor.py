import pygame

from robot.sensor import Sensor

class ColorSensor(Sensor):
    '''
    Class for the robot color sensors.
    '''

    def __init__(self, base):
        '''
        Initialize the color sensor.

        :param base: the robot which it is on
        '''
        super().__init__(base)
        pygame.draw.rect(self.surf, (100, 0, 0), (0, 0, 25, 8))
        pygame.draw.rect(self.surf, (100, 0, 0), (0, 0, 8, 25))
        pygame.draw.rect(self.surf, (100, 0, 0), (0, 17, 25, 8))
        pygame.draw.rect(self.surf, (100, 0, 0), (17, 0, 8, 25))

    def check_color(self, color):
        '''
        Check if the color that the sensor sees is the same as the
        given color.

        :param color: the color to check with
        :return: whether or not they are equal
        '''
        x = round(self.center_x)
        y = round(self.center_y)

        if self.base.grid[x][y] == color:
            return True
        return False

    def check_color_in_range(self, min, max):
        '''
        Check if the color that the sensor sees is in a given range.

        :param min: minimum RGB value for the range
        :param max: maximum RGB value for the range
        :return: whether or not it is in the range
        '''
        x = round(self.center_x)
        y = round(self.center_y)

        red = self.base.grid[x][y][0]
        green = self.base.grid[x][y][1]
        blue = self.base.grid[x][y][2]

        if red >= min[0] and red <= max[0]:
            if green >= min[1] and green <= max[1]:
                if blue >= min[2] and blue <= max[2]:
                    return True
        return False

    def __repr__(self):
        '''
        String representation for the sensor.

        :return: the string 'Color Sensor'
        '''
        return 'Color Sensor'