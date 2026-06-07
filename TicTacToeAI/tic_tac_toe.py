# Tic Tac Toe AI
# Created by Ayush Padwekar

player = "X"
computer = "O"

board = [" " for i in range(9)]


def show_positions():
    print("\nPosition Guide")
    print("1 | 2 | 3")
    print("---------")
    print("4 | 5 | 6")
    print("---------")
    print("7 | 8 | 9")
    print()


def show_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()


# check if someone wins
def check_winner(symbol):

    win_patterns = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for pattern in win_patterns:
        if (
            board[pattern[0]] == symbol and
            board[pattern[1]] == symbol and
            board[pattern[2]] == symbol
        ):
            return True

    return False


def is_board_full():
    return " " not in board


# player's move
def player_move():

    while True:

        try:
            move = int(input("Enter your move (1-9): ")) - 1

            if move < 0 or move > 8:
                print("Please enter a number between 1 and 9.")
                continue

            if board[move] != " ":
                print("This position is already taken.")
                continue

            board[move] = player
            break

        except ValueError:
            print("Invalid input. Please enter a number.")


# minimax algorithm
def minimax(is_maximizing):

    if check_winner(computer):
        return 1

    if check_winner(player):
        return -1

    if is_board_full():
        return 0

    if is_maximizing:

        best_score = -100

        for i in range(9):

            if board[i] == " ":

                board[i] = computer

                score = minimax(False)

                board[i] = " "

                if score > best_score:
                    best_score = score

        return best_score

    else:

        best_score = 100

        for i in range(9):

            if board[i] == " ":

                board[i] = player

                score = minimax(True)

                board[i] = " "

                if score < best_score:
                    best_score = score

        return best_score


# computer finds best move
def computer_move():

    best_score = -100
    best_move = 0

    for i in range(9):

        if board[i] == " ":

            board[i] = computer

            score = minimax(False)

            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = computer

    print("\nComputer chose:", best_move + 1)


print("=" * 40)
print(" TIC TAC TOE - HUMAN VS COMPUTER ")
print("=" * 40)

show_positions()

while True:

    show_board()

    player_move()

    if check_winner(player):
        show_board()
        print("🎉 Congratulations! You Win!")
        break

    if is_board_full():
        show_board()
        print("🤝 Match Draw!")
        break

    computer_move()

    if check_winner(computer):
        show_board()
        print("🤖 Computer Wins!")
        break

    if is_board_full():
        show_board()
        print("🤝 Match Draw!")
        break