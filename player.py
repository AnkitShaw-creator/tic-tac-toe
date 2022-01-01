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

class GeniusComputerPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)
    
    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())

        else:
            # get square of the minimax algorithm
            square = self.minimax(game, self.letter)['position'] # we only need the position of the best possible move
        return square

    def minimax(self, state, player):  # state = current state of the game
        max_player = self.letter # caller of the function
        other_player = 'O' if player == 'X' else 'X'

        # first we need to check whether our previous move was a winning move or not
        if state.Winner == other_player:
            return {
                'position': None,
                'score': 1*(state.num_empty_squares()+1) if other_player == max_player else -1*(state.num_empty_squares()+1)
            }

        elif not state.empty_squares():
            # there are no empty squares left then it is a tie
            return {'position': None, 'score': 0}
        
        if player == max_player:
            best = {'position': None, 'score': -math.inf} #each score should maximize, if you are the max_player
        else:
            best = {'position': None, 'score': math.inf} # each score(opponent) should minimize, if you opponent is the max player

        for possible_moves in state.available_moves():
            # first, we should try the moves
            state.make_move(possible_moves, player)
            # second, recurse through the minimax after trying the move
            simulated_move = self.minimax(state, other_player)
            # third, undo the move for future iteration so that we could try other moves
            state.board[possible_moves]=' '
            state.Winner = None
            simulated_move['position'] = possible_moves # may get messed up due to recursion
            # forth, update the dictionaries if needed, which should only happen if the current move beats the previous best score move
            if player == max_player: # to maximize our score
                if simulated_move['score'] > best['score']:
                    best = simulated_move # replacing the previous best move with the current best move
            else: # minimize the other player score 
                if simulated_move['score'] < best['score']:
                    best = simulated_move
        
        return best