class Solution:
    def __init__(self, assignments: dict):
        self.assignments = assignments
        self.cost = None

    def copy(self):
        return Solution(assignments=self.assignments.copy())