import random

class Player: 

    def __init__(self, name, score):
        self.score = score
        self.name = name
        self.players = []

    def get_score(self):
        return self.score 