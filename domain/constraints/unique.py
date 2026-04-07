from domain.constraints.constraint import Constraint


class UniqueConstraint(Constraint):
    def __init__(self, attr, penalty=10, weight=1):
        super().__init__(weight)
        self.attr = attr
        self.penalty = penalty

    def evaluate(self, solution, nodes):
        seen = set()
        penalty = 0

        for node in nodes:
            value = node.get(self.attr)

            if value in seen:
                penalty += self.penalty
            else:
                seen.add(value)

        return penalty * self.weight