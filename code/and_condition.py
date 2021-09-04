from code.condition import Condition


class AndCondition(Condition):
    def __init__(self, condition1, condition2):
        self.condition1 = condition1
        self.condition2 = condition2

    def setup(self):
        try:
            self.condition1.setup()
        except:
            pass
        try:
            self.condition2.setup()
        except:
            pass

    def is_met(self):
        return self.condition1.is_met() and self.condition2.is_met()