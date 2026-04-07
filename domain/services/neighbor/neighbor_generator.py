import random


class NeighborGenerator:
    def __init__(self, moves):
        self.moves = moves

    def generate(self, solution):
        if not self.moves:
            return solution.copy()
        
        new_solution = solution.copy()

        num_moves = random.randint(1, 3)

        for _ in range(num_moves):
            move = random.choice(self.moves)
            move.apply(new_solution)

        return new_solution