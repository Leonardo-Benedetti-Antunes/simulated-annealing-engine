import random

from domain.services.neighbor.moves.move import Move


class ShuffleMove(Move):
    def __init__(self, list_attr):
        self.list_attr = list_attr

    def apply(self, solution):
        nodes = getattr(solution, self.list_attr, [])

        if not nodes:
            return

        node = random.choice(nodes)

        if not hasattr(node, "items"):
            return

        random.shuffle(node.items)