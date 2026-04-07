import random

from domain.services.neighbor.moves.move import Move


class MoveItemMove(Move):
    def __init__(self, list_attr):
        self.list_attr = list_attr

    def apply(self, solution):
        nodes = getattr(solution, self.list_attr, [])

        if len(nodes) < 2:
            return

        source, target = random.sample(nodes, 2)

        if not hasattr(source, "items") or not hasattr(target, "items"):
            return

        if not source.items:
            return

        i = random.randrange(len(source.items))
        item = source.items.pop(i)

        target.items.append(item)