from code.directions import TurnDirection


class SimpleTurnBlock:
    '''
    Class for a turn block within a loop.
    '''

    def __init__(self, display, target, direction, speed):
        '''
        Create a new simple turn block.

        :param display: the display to update
        :param target: the robot to turn
        :param direction: the direction to turn
        :param speed: the speed at which to turn
        '''
        self.display = display
        self.target = target

        self.direction = direction
        self.speed = speed

    def execute(self):
        '''
        Execute the turn once.

        :return: None
        '''
        if self.direction == TurnDirection.CLOCKWISE:
            self.target.turn_cw(self.speed)
        else:
            self.target.turn_counter_cw(self.speed)