import random as rd
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.count = 0

    def display(self):
        print("\t",self.name, ": ", self.count)

    def choose(self, opp_prev):
        if (rd.randint(0, 1) < 0.5):
            return True
        else:
            return False
        
    def clone(self):
        return self.__class__(self.name)
        
class PassivePlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def choose(self, opp_prev):
        if (rd.randint(0, 1) < 0.2):
            return True
        else:
            return False

class AggressivePlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def choose(self, opp_prev):
        if (rd.randint(0, 1) < 0.8):
            return True
        else:
            return False

class TitForTatPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def choose(self, opp_prev=False):
        return opp_prev

def prisoner_dilemma(player1, snitch1, player2, snitch2, show=False):
    if snitch1 and snitch2:
        player1.count += 2
        player2.count += 2
    elif snitch1 and not snitch2:
        player1.count += 0
        player2.count += 3
    elif not snitch1 and snitch2:
        player1.count += 3
        player2.count += 0
    elif not snitch1 and not snitch2:
        player1.count += 1
        player2.count += 1
    
    if (show):
        print(player1.name, ": ", snitch1," --- ", player2.name, ": ", snitch2)

def epoch(player1, player2, num_epochs, show=False):
    c1, c2 = False, False
    for i in range(0, num_epochs):
        c1 = player1.choose(c2)
        c2 = player2.choose(c1)
        prisoner_dilemma(player1, c1, player2, c2)

        if (show):
            print("\nEPOCH:", i)
            player1.display()
            player2.display()

def main():
    rd.seed(time.time())
    players = [
        Player('Bal'), 
        PassivePlayer('Pas'), 
        AggressivePlayer('Agg'), 
        TitForTatPlayer('Tft')
        ]

    totals = [0, 0, 0, 0]

    for p1 in players:
        for p2 in players:
            equals = False
            if (players.index(p1) == players.index(p2)):
                equals = True
                p2 = p1.clone()

            epoch(p1, p2, 10000)

            win = ""
            if (p1.count < p2.count):
                win = p1.name
            elif (p2.count < p1.count):
                win = p2.name
            
            print(p1.name, "vs", p2.name, ":", p1.count, ",", p2.count, "-", win)
            
            totals[players.index(p1)] += p1.count
            p1.count = 0
            if (not equals):
                totals[players.index(p2)] += p2.count
                p2.count = 0
    
    print("")

    for t in totals:
        print(players[totals.index(t)].name, ":", t)


main()