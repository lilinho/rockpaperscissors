"""
figures.py

Defines classes of each figure used in game. Each figure have its own id and name.
It also has dictionary of figures defeated by it, where key is id of defeated figure and value is short description

File contains also definition of Player class (name field and wins field

"""

class Scissors:
    def __init__(self):
        self.id = 0
        self.defeats = {2: "Scissors cuts Paper", 4: "Scissors decapitates Lizard"}
        self.name = "Scissors"


class Rock:
    def __init__(self):
        self.id = 1
        self.defeats = {0: "Rock crushes Scissors", 4: "Rock crushes Lizard"}
        self.name = "Rock"


class Paper:
    def __init__(self):
        self.id = 2
        self.defeats = {1: "Paper covers Rock", 3: "Paper disproves Spock"}
        self.name = "Paper"


class Spock:
    def __init__(self):
        self.id = 3
        self.defeats = {0: "Spock smashes Scissors", 1: "Spock vaporizes Rock"}
        self.name = "Spock"


class Lizard:
    def __init__(self):
        self.id = 4
        self.defeats = {2: " Lizard eats Paper", 3: "Lizard poisons Spock"}
        self.name = "Lizard"


class Player:
    def __init__(self, n="Computer"):
        self.name = n
        self.wins = 0
