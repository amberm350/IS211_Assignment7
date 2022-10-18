import argparse
import random


def throw_the_die(sides=6):

    return random.randint(1, sides)


class Player:
    def __init__(self, name):
        self.name = name
        self.total = 0

    def show(self):
        print(f"{self}")

    def __str__(self):
        
        return f"{self.name}'s Total = {self.total}"

    def turn(self):
        
        turn_total = 0
        roll_hold = ''
        while roll_hold != "h":
            die = throw_the_die()
            if die == 1:
                print ("You rolled a 1, next players turn")
            
                break

            
            turn_total += die
            print (f"The turn total is {turn_total}")
            print (f"The possible total if you hold is {self.total + turn_total}")
            print (f"The real total is {die}")
    
            roll_hold = input("Roll(r) or Hold(h)? ").lower()

        if roll_hold == 'h':
            self.total += turn_total

        self.show()


class Game:
    
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.current_player= self.players[0]
        self.winner = None
    
    def check_winner(self):

        for player in self.players:
            if player.total >= 100:
                self.winner = player
                return True

        return False
    
    def change_player(self):

        if self.current_player == self.players[0]:

            self.current_player = self.players[1]
        else:
            self.current_player = self.players[0]

    def play_game(self):
        
        self.current_player = self.players[0]
        while not self.check_winner():
            
            self.current_player.turn()
            
            self.change_player()
            print (self.current_player)
        

        self.winner.show()

if __name__ == '__main__':
    p1 = Player("John")
    p2 = Player("Jane")
    pig_game = Game(p1, p2)
    pig_game.play_game()