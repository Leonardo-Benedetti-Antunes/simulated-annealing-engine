import math
import random

class SimulatedAnnealing:

    def __init__(self, cost_calculator, neighbor_generator, initial_temp=1000, cooling_rate=0.95):
        self.cost_calculator = cost_calculator
        self.neighbor_generator = neighbor_generator
        self.temperature = initial_temp
        self.cooling_rate = cooling_rate

    def optimize(self, initial_solution):

        current = initial_solution
        current.cost = self.cost_calculator.calculate(current)

        best = current

        while self.temperature > 0.1:

            neighbor = self.neighbor_generator.generate(current)
            neighbor.cost = self.cost_calculator.calculate(neighbor)

            delta = neighbor.cost - current.cost

            if delta < 0:
                current = neighbor
            else:
                probability = math.exp(-delta / self.temperature)
                if random.random() < probability:
                    current = neighbor

            if current.cost < best.cost:
                best = current

            self.temperature *= self.cooling_rate

        return best