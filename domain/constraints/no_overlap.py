from domain.constraints.constraint import Constraint


class NoOverlapConstraint(Constraint):
    def __init__(self, start_attr, end_attr, penalty=10, weight=1):
        super().__init__(weight)
        self.start_attr = start_attr
        self.end_attr = end_attr
        self.penalty = penalty

    def evaluate(self, solution, nodes):
        penalty = 0

        intervals = []

        for node in nodes:
            start = node.get(self.start_attr)
            end = node.get(self.end_attr)

            if start is None or end is None:
                continue

            for s, e in intervals:
                if not (end <= s or start >= e):
                    penalty += self.penalty

            intervals.append((start, end))

        return penalty * self.weight