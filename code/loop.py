import pygame


class Loop:
    '''
    Class to control loops in the flow of a program.
    '''

    def __init__(self, display, target, upper_loop):
        '''
        Initialize the loop.

        :param display: the display to update
        :param target: the robot
        :param upper_loop: the loop directly above, if it exists
        '''
        self.display = display
        self.target = target
        self.upper_loop = upper_loop
        self.actions = []

    def add_condition(self, condition):
        '''
        Add a condition to the loop.

        :param condition: the condition to stop at
        :return: None
        '''
        self.condition = condition

    def add_new_condition(self, condition_class, new_condition):
        '''
        Add a condition to the existing condition.

        :param condition_class: the operator to join the conditions
        :param new_condition: the additional condition
        :return: None
        '''
        self.condition = condition_class(self.condition, new_condition)

    def add_action(self, action):
        '''
        Add an action to the sequence.

        :param action: the action to add
        :return: None
        '''
        self.actions.append(action)

    def execute(self):
        '''
        Execute the sequence repeatedly until the terminating condition is met.
        :return:
        '''
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
        '''
        Check if the condition is met.

        :return: the truth value of the condition
        '''
        return self.condition.is_met()