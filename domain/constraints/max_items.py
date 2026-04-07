from domain.constraints.constraint import Constraint


class MaxItemsConstraint(Constraint):
    def __init__(self, max_items, penalty=10, weight=1):
        super().__init__(weight)
        self.max_items = max_items
        self.penalty = penalty

    def evaluate(self, solution, nodes):
        penalty = 0

        for node in nodes:
            if node.has("items"):
                if len(node.items) > self.max_items:
                    penalty += self.penalty

        return penalty * self.weight