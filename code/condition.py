class Condition:
    '''
    Abstract class for conditions.
    '''

    def __init__(self, condition):
        '''
        Initialize the condition.

        :param condition: the type of condition.
        '''
        self.condition = condition
        self.met = False

    def is_met(self):
        '''
        Check whether the condition is met.

        :return: the truth value of the condition
        '''
        return self.met

    def meet(self):
        '''
        Set the truth value to true.

        :return: None
        '''
        self.met = True

    def unmeet(self):
        '''
        Set the truth value to false.

        :return: None
        '''
        self.met = False