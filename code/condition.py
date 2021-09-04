class Condition:
    def __init__(self, condition):
        self.condition = condition
        self.met = False

    def is_met(self):
        return self.met

    def meet(self):
        self.met = True

    def unmeet(self):
        self.met = False