from func.trig import *
from robot.sensor import Sensor

class TouchSensor(Sensor):
    '''
    Class for the robot touch sensors.
    '''

    def __init__(self, base):
        '''
        Initialize the touch sensor.

        :param base: the robot which it is on
        '''
        super().__init__(base)
        self.surf.fill((0, 255, 0))

    def check_touched(self, mouse):
        '''
        Check whether or not the mouse is on the sensor.

        :param mouse: the pygame mouse
        :return: whether the mouse is on the sensor or not
        '''
        if math.cos(math.radians(self.direction)) != 0 and math.sin(math.radians(self.direction)) != 0:
            if mouse[1] >= self.y + self.width * math.fabs(math.sin(math.radians(self.direction))) - \
                    (mouse[0] - self.x) * math.fabs(math.tan(math.radians(self.direction))):
                if mouse[1] <= self.y + self.width * (sin_abs_deg(self.direction) + cos_abs_deg(self.direction)) - \
                        (mouse[0] - self.x - self.width * sin_abs_deg(self.direction)) * tan_abs_deg(self.direction):
                    if mouse[1] <= self.y + self.width * sin_abs_deg(self.direction) + \
                            (mouse[0] - self.x) / tan_abs_deg(self.direction):
                        if mouse[1] >= self.y + (mouse[0] - self.x - self.width * cos_abs_deg(self.direction)) / \
                                tan_abs_deg(self.direction):
                            return True
        else:
            if mouse[0] >= self.x and mouse[0] <= self.x + self.width:
                if mouse[1] >= self.y and mouse[1] <= self.y + self.width:
                    return True

    def __repr__(self):
        '''
        String representation of touch sensor.

        :return: the string 'Touch Sensor'
        '''
        return 'Touch Sensor'