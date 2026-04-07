class CostCalculator:

    def __init__(self, layers):
        self.layers = layers

    def calculate(self, solution):
        return sum(layer.evaluate(solution) for layer in self.layers)