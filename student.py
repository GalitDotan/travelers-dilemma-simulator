class Student:
    def __init__(self, choice: int):
        self.choice: int = choice
        self.sum_utility: int = 0
        self.games_count: int = 0

    def __repr__(self):
        return f"Choice: {self.choice}, Average utility: {self.average_utility()}"

    def average_utility(self):
        if self.games_count == 0:
            return 0
        return self.sum_utility / self.games_count
