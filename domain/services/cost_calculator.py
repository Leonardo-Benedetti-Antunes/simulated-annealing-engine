class CostCalculator:

    def __init__(self, constraints):
        self.constraints = constraints

    def calculate(self, solution):
        total_cost = 0

        for constraint in self.constraints:
            total_cost += constraint.evaluate(solution)

        return total_cost