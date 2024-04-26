class GameLogic:
    def __init__(self):
        self.game_board = [[' ']*3 for _ in range(3)]

    def print_game_board(self):
        for row in self.game_board:
            print('|', end='')
            for cell in row:
                print(cell, end='|')
            print()

    def check_for_winner(self):
        # Check rows
        for row in self.game_board:
            if row[0] == row[1] == row[2] and row[0] != ' ':
                return row[0]
        # Check columns
        for col in range(3):
            if self.game_board[0][col] == self.game_board[1][col] == self.game_board[2][col] and self.game_board[0][col] != ' ':
                return self.game_board[0][col]
        # Check diagonals
        if self.game_board[0][0] == self.game_board[1][1] == self.game_board[2][2] and self.game_board[0][0] != ' ':
            return self.game_board[0][0]
        if self.game_board[0][2] == self.game_board[1][1] == self.game_board[2][0] and self.game_board[0][2] != ' ':
            return self.game_board[0][2]
        # Check for a draw
        if all(cell != ' ' for row in self.game_board for cell in row):
            return 'draw'
        return None

    def make_move(self, row, col, symbol):
        if self.game_board[row][col] == ' ':
            self.game_board[row][col] = symbol
            return True
        else:
            print("Invalid move. Please try again.")
            return False

def print_game_board(game_board):
    for row in game_board:
        print('|', end='')
        for cell in row:
            print(cell, end='|')
        print()

def check_for_winner(game_board):
    # Check rows
    for row in game_board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]
    # Check columns
    for col in range(3):
        if game_board[0][col] == game_board[1][col] == game_board[2][col] and game_board[0][col] != ' ':
            return game_board[0][col]
    # Check diagonals
    if game_board[0][0] == game_board[1][1] == game_board[2][2] and game_board[0][0] != ' ':
        return game_board[0][0]
    if game_board[0][2] == game_board[1][1] == game_board[2][0] and game_board[0][2] != ' ':
        return game_board[0][2]
    # Check for a draw
    if all(cell != ' ' for row in game_board for cell in row):
        return 'draw'
    return None
