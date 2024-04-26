from logic import print_game_board, check_for_winner
from ai import find_best_move

def main():
    print("Welcome to Tic Tac Toe")
    print("----------------------")

    game_board = [[' ']*3 for _ in range(3)]

    while True:
        print_game_board(game_board)
        player_move = int(input("\nChoose a number [1-9]: "))
        row, col = (player_move-1) // 3, (player_move-1) % 3
        if game_board[row][col] == ' ':
            game_board[row][col] = 'X'
        else:
            print("Invalid move. Please try again.")
            continue

        winner = check_for_winner(game_board)
        if winner:
            if winner == 'draw':
                print_game_board(game_board)
                print("\nIt's a draw! Thank you for playing :)")
            else:
                print_game_board(game_board)
                print("\n{} has won! Thank you for playing :)".format(winner))
            break

        print("AI's turn...")
        ai_row, ai_col = find_best_move(game_board)
        game_board[ai_row][ai_col] = 'O'

        winner = check_for_winner(game_board)
        if winner:
            print_game_board(game_board)
            if winner == 'draw':
                print("\nIt's a draw! Thank you for playing :)")
            else:
                print("\n{} has won! Thank you for playing :)".format(winner))
            break

if __name__ == "__main__":
    main()
