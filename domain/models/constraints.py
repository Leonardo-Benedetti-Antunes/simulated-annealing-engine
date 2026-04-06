from abc import ABC, abstractmethod

class Constraint(ABC):

    @abstractmethod
    def evaluate(self, solution: "Solution") -> float:
        pass