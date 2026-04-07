class Constraint:
    def __init__(self, weight=1):
        self.weight = weight

    def evaluate(self, solution, nodes):
        raise NotImplementedError

    def apply_weight(self, value):
        return value * self.weight