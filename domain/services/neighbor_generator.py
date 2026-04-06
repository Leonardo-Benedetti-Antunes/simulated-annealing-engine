import random

class NeighborGenerator:

    def __init__(self, possible_values):
        self.possible_values = possible_values

    def generate(self, solution):
        new_solution = solution.copy()

        key = random.choice(list(new_solution.assignments.keys()))
        new_solution.assignments[key] = random.choice(self.possible_values)

        return new_solution