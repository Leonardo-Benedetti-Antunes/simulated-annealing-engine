import random

from domain.services.neighbor.moves.move import Move


class SwapMove(Move):
    def __init__(self, list_attr):
        self.list_attr = list_attr

    def apply(self, solution):
        nodes = getattr(solution, self.list_attr, [])

        if len(nodes) < 2:
            return

        n1, n2 = random.sample(nodes, 2)

        if not hasattr(n1, "items") or not hasattr(n2, "items"):
            return

        if not n1.items or not n2.items:
            return

        i = random.randrange(len(n1.items))
        j = random.randrange(len(n2.items))

        n1.items[i], n2.items[j] = n2.items[j], n1.items[i]