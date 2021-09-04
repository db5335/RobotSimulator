from code.directions import TurnDirection


class SimpleTurnBlock:
    def __init__(self, display, target, direction, speed):
        self.display = display
        self.target = target

        self.direction = direction
        self.speed = speed

    def execute(self):
        if self.direction == TurnDirection.CLOCKWISE:
            self.target.turn_cw(self.speed)
        else:
            self.target.turn_counter_cw(self.speed)