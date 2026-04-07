from domain.constraints.not_empty import NotEmptyConstraint
from domain.models.solution import Solution
from domain.models.node import Node

from domain.constraints.constraint import Constraint
from domain.constraints.constraint_layer import ConstraintLayer

from domain.services.neighbor.moves.move_item_move import MoveItemMove
from domain.services.neighbor.moves.swap_move import SwapMove
from domain.services.neighbor.neighbor_generator import NeighborGenerator
from engine.evaluation.evaluator import Evaluator
from engine.simulated_annealing.simulated_annealing import SimulatedAnnealing


def test_simulated_annealing_improves_solution():
    turmas = [
        Node({"items":["A", "B"]}),
        Node({"items":[]}),
        Node({"items":[]}),
    ]

    solution = Solution(turmas=turmas)

    layer = ConstraintLayer(
        name="turmas",
        constraints=[NotEmptyConstraint(penalty=10)],
        node_selector=lambda s: s.turmas
    )

    evaluator = Evaluator([layer])

    moves = [
        MoveItemMove("turmas"),
        SwapMove("turmas"),
    ]

    generator = NeighborGenerator(moves)

    sa = SimulatedAnnealing(
        evaluator=evaluator,
        neighbor_generator=generator,
        initial_temperature=100,
        cooling_rate=0.95,
        max_iterations=200
    )

    initial_cost = evaluator.evaluate(solution)

    best_solution, best_cost = sa.run(solution)

    print("Initial:", initial_cost)
    print("Final:", best_cost)

    assert best_cost <= initial_cost

test_simulated_annealing_improves_solution()