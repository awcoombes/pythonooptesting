class Participant:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.choice = ""
    def choose(self):
        self.choice = input("{name}, select r, p, sc, l or sp: ".format(name = self.name))
        choiceconv = {"r": "rock", "p": "paper", "sc": "scissors", "l": "lizard", "sp": "spock"}
        print("{name} chooses {choice}".format(name = self.name, choice = choiceconv[self.choice]))
    def tonumericalchoice(self):
        switcher = {"r": 0, "p": 1, "sc": 2, "l": 3, "sp": 4}
        return switcher[self.choice]
    def incrementpoints(self):
        self.points += 1

class GameRound:
    def __init__(self, p1, p2):
        self.rules = [[0, -1, 1, 1, -1], [1, 0, -1, -1, 1], [-1, 1, 0, 1, -1], [-1, 1, -1, 0, 1], [1, -1, 1, -1, 0]]
        p1.choose()
        p2.choose()
        result = self.comparechoices(p1, p2)
        print("Round resulted in a {result}".format(result = self.getresultasastring(result)))
        if result > 0:
            p1.incrementpoints()
        elif result < 0:
            p2.incrementpoints()
    def comparechoices(self, p1, p2):
        return self.rules[p1.tonumericalchoice()][p2.tonumericalchoice()]
    def getresultasastring(self, result):
        res = {0: "draw", 1: "win", -1: "loss"}
        return res[result]
    def awardpoints(self):
        print("implement")

class Game:
    def __init__(self):
        self.endgame = False
        self.participant = Participant("Andrew")
        self.secondparticipant = Participant("Computer")
    def determineWinner(self):
        resultString = "It's a Draw"
        if self.participant.points > self.secondparticipant.points:
            resultString = "Winner is {name}".format(name=self.participant.name)
        elif self.participant.points < self.secondparticipant.points:
            resultString = "Winner is {name}".format(name=self.secondparticipant.name)
        print(resultString)
    def checkEndCondition(self):
        answer = input("Continue game y/n ")
        if answer == 'y':
            GameRound(self.participant, self.secondparticipant)
            self.checkEndCondition()
        else:
            print("Game ended, {p1name} has {p1points}, and {p2name} has {p2points}".format(p1name = self.participant.name, p1points= self.participant.points, p2name=self.secondparticipant.name, p2points=self.secondparticipant.points))
            self.determineWinner()
            self.endgame = True
    def start(self):
        while not self.endgame:
            GameRound(self.participant, self.secondparticipant)
            self.checkEndCondition()

game = Game()
game.start()