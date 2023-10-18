class Player:

    def __init__(self, name, total_score=0):
        self.name = name
        self.total_score = total_score

    def __str__(self):
        return f'Name: {self.name} total score: {self.total_score}'

    # getter methods
    def get_name(self):
        return self.name

    def get_total_score(self):
        return self.total_score

    # setter method
    def set_total_score(self, turn_score):
        self.total_score += turn_score
