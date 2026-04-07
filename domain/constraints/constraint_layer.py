class ConstraintLayer:
    def __init__(self, name, constraints, node_selector):
        self.name = name
        self.constraints = constraints
        self.node_selector = node_selector

    def evaluate(self, solution):
        total = 0

        nodes = self.node_selector(solution)

        for constraint in self.constraints:
            total += constraint.evaluate(solution, nodes)

        return total