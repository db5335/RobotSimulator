from robot.sensor import Sensor

class UltrasoundSensor(Sensor):
    '''
    Class for the robot ultrasound sensor.
    '''
    def __init__(self, base):
        '''
        Initialize the ultrasound sensor

        :param base: the robot which it is on
        '''
        super().__init__(base)
        self.surf.fill((255, 0, 155))

    def get_distance(self):
        '''
        Get the distance from the sensor to the nearest edge.
        :return:
        '''
        direction = self.direction % 360
        # TODO get distance from nearest edge

    def __repr__(self):
        '''
        String representation for the ultrasound sensor.

        :return: the string 'Ultrasound Sensor'
        '''
        return "Ultrasound Sensor"