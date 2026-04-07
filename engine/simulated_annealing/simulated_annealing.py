import math
import random


class SimulatedAnnealing:
    def __init__(
        self,
        evaluator,
        neighbor_generator,
        initial_temperature=1000,
        cooling_rate=0.95,
        min_temperature=0.01,
        max_iterations=1000
    ):
        self.evaluator = evaluator
        self.neighbor_generator = neighbor_generator
        self.initial_temperature = initial_temperature
        self.cooling_rate = cooling_rate
        self.min_temperature = min_temperature
        self.max_iterations = max_iterations

    def run(self, initial_solution):
        current_solution = initial_solution
        current_cost = self.evaluator.evaluate(current_solution)

        best_solution = current_solution
        best_cost = current_cost

        temperature = self.initial_temperature
        iteration = 0

        while temperature > self.min_temperature and iteration < self.max_iterations:

            new_solution = self.neighbor_generator.generate(current_solution)
            new_cost = self.evaluator.evaluate(new_solution)

            delta = new_cost - current_cost

            if self._accept(delta, temperature):
                current_solution = new_solution
                current_cost = new_cost

            if current_cost < best_cost:
                best_solution = current_solution
                best_cost = current_cost

            temperature *= self.cooling_rate
            iteration += 1

            print(f"Iter: {iteration} | Temp: {temperature:.2f} | Cost: {current_cost} | Best: {best_cost}")

        return best_solution, best_cost

    def _accept(self, delta, temperature):
        if delta < 0:
            return True

        probability = math.exp(-delta / temperature)
        return random.random() < probability