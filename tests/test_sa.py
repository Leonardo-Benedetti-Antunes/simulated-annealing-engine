from domain.models.solution import Solution
from domain.services.cost_calculator import CostCalculator
from domain.services.neighbor_generator import NeighborGenerator
from engine.simulated_annealing.sa_engine import SimulatedAnnealing
from domain.constraints.constraint import Constraint


class DifferentValuesConstraint(Constraint):
    def evaluate(self, solution):
        values = list(solution.assignments.values())
        return len(values) - len(set(values))  # penaliza duplicados


def run():

    initial = Solution({
        "a": 1,
        "b": 1,
        "c": 1
    })

    constraints = [DifferentValuesConstraint()]
    cost_calculator = CostCalculator(constraints)
    neighbor_generator = NeighborGenerator([1, 2, 3])

    sa = SimulatedAnnealing(cost_calculator, neighbor_generator)

    best = sa.optimize(initial)

    print("Best:", best.assignments)
    print("Cost:", best.cost)


if __name__ == "__main__":
    run()