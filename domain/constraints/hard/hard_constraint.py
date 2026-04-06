from domain.constraints.constraint import Constraint


class HardConstraint(Constraint):
    def evaluate(self, solution) -> float:
        return 0  # override nas implementações