from domain.constraints.constraint import Constraint


class NotEmptyConstraint(Constraint):
    def __init__(self, penalty=10, weight=1):
        super().__init__(weight)
        self.penalty = penalty

    def evaluate(self, solution, nodes):
        penalty = 0

        for node in nodes:
            if self._is_empty(node):
                penalty += self.penalty

        return penalty * self.weight

    def _is_empty(self, node):
        items = node.get("items")

        if items is not None:
            return len(items) == 0

        value = node.get("value")
        return value is None