from logic import check_for_winner

def minimax(depth, is_maximizing, game_board):
    result = check_for_winner(game_board)
    if result:
        if result == 'X':
            return -1
        elif result == 'O':
            return 1
        else:
            return 0

    if is_maximizing:
        best_score = float('-inf')
        for i in range(3):
            for j in range(3):
                if game_board[i][j] == ' ':
                    game_board[i][j] = 'O'
                    score = minimax(depth+1, False, game_board)
                    game_board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if game_board[i][j] == ' ':
                    game_board[i][j] = 'X'
                    score = minimax(depth+1, True, game_board)
                    game_board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

def find_best_move(game_board):
    best_score = float('-inf')
    move = None
    for i in range(3):
        for j in range(3):
            if game_board[i][j] == ' ':
                game_board[i][j] = 'O'
                score = minimax(0, False, game_board)
                game_board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move
