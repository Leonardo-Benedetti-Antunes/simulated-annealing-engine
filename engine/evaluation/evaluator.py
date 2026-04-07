class Evaluator:
    def __init__(self, layers):
        self.layers = layers

    def evaluate(self, solution):
        total_cost = 0

        for layer in self.layers:
            nodes = layer.node_selector(solution)

            for constraint in layer.constraints:
                cost = constraint.evaluate(solution, nodes)
                total_cost += cost

        return total_cost