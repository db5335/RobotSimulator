from code.directions import MoveDirection


class SimpleMoveBlock:
    def __init__(self, display, target, direction, speed):
        self.display = display
        self.target = target

        self.direction = direction
        self.speed = speed

    def execute(self):
        if self.direction == MoveDirection.FORWARD:
            self.target.move_forward(self.speed)
        else:
            self.target.move_backward(self.speed)