class Participant:
    def __init__(self):
        self.points = 0
        self.choice = ""

#class GameRound:
    # test

class Game:
    def __init__(self):
        self.endgame = False
        self.participant = Participant()
        self.secondparticipant = Participant()