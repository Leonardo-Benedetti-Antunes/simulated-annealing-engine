from domain.constraints.constraint import Constraint


class MinItemsConstraint(Constraint):
    def __init__(self, min_items, penalty=10, weight=1):
        super().__init__(weight)
        self.min_items = min_items
        self.penalty = penalty

    def evaluate(self, solution, nodes):
        penalty = 0

        for node in nodes:
            if node.has("items"):
                if len(node.items) < self.min_items:
                    penalty += self.penalty

        return penalty * self.weight