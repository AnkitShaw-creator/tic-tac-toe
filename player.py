import math
import random

class Player():
    def __init__(self, letter):
        self.letter = letter
    
    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        valid_move = False
        val = None
        while not valid_move:
            square = input(self.letter+'\'s turn. Input move(0-8): ')

            # check whether the user input is valid or not
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_move= True # if the user input is valid
            except ValueError:
                print('Invalid move! Please try again')
        
        return val