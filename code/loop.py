import pygame


class Loop:
    def __init__(self, display, target, upper_loop):
        self.display = display
        self.target = target
        self.upper_loop = upper_loop
        self.actions = []

    def add_condition(self, condition):
        self.condition = condition

    def add_new_condition(self, condition_class, new_condition):
        self.condition = condition_class(self.condition, new_condition)

    def add_action(self, action):
        self.actions.append(action)

    def execute(self):
        try:
            self.condition.setup()
        except:
            pass

        py_clock = pygame.time.Clock()

        while True:
            if self.check_condition():
                break
            for action in self.actions:
                action.execute()
            self.display.blit(self.target.background, (0, 0))
            self.display.blit(self.target.surf, (self.target.x, self.target.y))
            py_clock.tick(100)
            pygame.display.update()

    def check_condition(self):
        return self.condition.is_met()