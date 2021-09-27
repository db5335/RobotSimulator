from code.directions import MoveDirection


class SimpleMoveBlock:
    '''
    Class for a move block within a loop.
    '''

    def __init__(self, display, target, direction, speed):
        '''
        Create a new simple move block.

        :param display: the display to update
        :param target: the robot to move
        :param direction: the direction to move
        :param speed: the speed at which to move
        '''
        self.display = display
        self.target = target

        self.direction = direction
        self.speed = speed

    def execute(self):
        '''
        Execute the move once.
        :return:
        '''
        if self.direction == MoveDirection.FORWARD:
            self.target.move_forward(self.speed)
        else:
            self.target.move_backward(self.speed)