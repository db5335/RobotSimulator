from code.condition import Condition


class AndCondition(Condition):
    '''
    Class representing the logical AND operator.
    '''

    def __init__(self, condition1, condition2):
        '''
        Initialize both operands.

        :param condition1: first operand
        :param condition2: second operand
        '''
        self.condition1 = condition1
        self.condition2 = condition2

    def setup(self):
        '''
        Setup both operands if necessary.

        :return: None
        '''
        try:
            self.condition1.setup()
        except:
            pass
        try:
            self.condition2.setup()
        except:
            pass

    def is_met(self):
        '''
        Check whether the condition is met.

        :return: the truth value of the AND condition
        '''
        return self.condition1.is_met() and self.condition2.is_met()