import random

from domain.services.neighbor.moves.move import Move


class ChangeAttributeMove(Move):
    def __init__(self, list_attr, attr_name, delta_options):
        self.list_attr = list_attr
        self.attr_name = attr_name
        self.delta_options = delta_options

    def apply(self, solution):
        nodes = getattr(solution, self.list_attr, [])

        if not nodes:
            return

        node = random.choice(nodes)

        if not hasattr(node, self.attr_name):
            return

        delta = random.choice(self.delta_options)

        current = getattr(node, self.attr_name)
        setattr(node, self.attr_name, current + delta)