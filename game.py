import player


class TicTacToe():
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.Winner = None # keep track of the winner

    def print_board(self):
        for row in [self.board[i*3: (i+1)*3] for i in range(3)]:
            print('|'+'|'.join(row)+'|')

    @staticmethod
    def print_board_nums():
        # print the board with the index of the position each box
        number_board =[[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('|'+'|'.join(row)+'|')

    def available_moves(self):
        # print the index of the box that are not filled yet
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        
    
    def empty_squares(self):
        return ' ' in self.board # will return a boolean if there are empty boxes in the board
    
    def num_empty_squares(self):
        return self.board.count(' ') # will return the number of empty spaces in the board

    def make_move(self, square, letter):
        if self.board[square]==' ':
            self.board[square] = letter
            if self.check_winner(square, letter):
                self.Winner = letter
            return True

        return False

    def check_winner(self, square, letter):
        # check if the letter in the rows are same
        row_index = square // 3
        row = self.board[row_index*3: (row_index +1)*3]
        if all([spot == letter for spot in row]):
            return True

        col_index = square % 3
        column = [self.board[col_index+i*3]  for i in range(3)]
        if all([spot == letter for spot in row]):
            return True

        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]] # left to right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True

            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all([spot == letter for spot in row]):
                return True

        return False


        
def play(game, player_o, player_x, print_game=True):
    if print_game:
        # print the moves
        game.print_board_nums()
    letter = 'X'
    while game.empty_squares():
        if letter == 'X':
            square = player_x.get_move(game)
        else:
            square = player_o.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter+ f'makes a move to square{square}')
                game.print_board()
                print('')

            if game.Winner:
                print(f'{game.Winner} is the winner!')

            letter = 'O' if letter == 'X' else 'X'
        else:
            print('Invalid move!')


    if print_game:
        print("It's a tie!")



if __name__ == "__main__":
    x_player = player.HumanPlayer('X')
    o_player = player.RandomComputerPlayer('O')

    t = TicTacToe()

    play(t, o_player, x_player, print_game=True)