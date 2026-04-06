from domain.constraints.constraint import Constraint


class SoftConstraint(Constraint):

    def __init__(self, weight: float = 1.0):
        self.weight = weight

    def evaluate(self, solution) -> float:
        return 0  # override