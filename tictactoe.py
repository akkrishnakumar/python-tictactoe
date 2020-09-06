# Tic Tac Toe - Python #
import random

board = list()

player = "X"
bot = "O"


def reset_board():
    global board
    board = list(
        map(
            lambda pos: " ",
            list(range(0, 9))
        )
    )


def separator():
    print(
        "".join(
            list(
                map(
                    lambda n: "-",
                    range(0, 100)
                )
            )
        )
    )


def print_instructions():
    separator()
    print("Enter position number (1-9) to play your move")
    print("Enter 'q' to exit")
    separator()


def print_game_separator(index):
    if index + 1 != 9:
        print("\n---|---|---")
    else:
        print("")


def print_position(value, separator=False):
    if separator:
        print(f" {value} ", end="|")
    else:
        print(f" {value} ", end="")


def empty_cell(cell):
    return cell.isspace()


def show_board():
    for index, value in enumerate(board):
        if (index + 1) % 3 != 0:
            print_position(value, True)
        else:
            print_position(value)
            print_game_separator(index)
    print("")


def validate_user_input(user_input):
    if user_input.isdigit() and int(user_input) in range(1, 10):
        return 1
    elif user_input.isalpha() and user_input == 'q':
        return 0
    else:
        return -1


def get_random_pos():
    return random.randint(1, 9)


def board_not_occupied():
    return " " in board


def check_consecutives():
    # TODO: Akhil - Need to improve the logic here

    # horizontal
    for row in [0, 3, 6]:
        curr = board[row]
        if curr == board[row+1] and curr == board[row+2] and not empty_cell(curr):
            return curr

    # vertical
    for col in [0, 1, 2]:
        curr = board[col]
        if curr == board[col+3] and curr == board[col+6] and not empty_cell(curr):
            return curr

    # cross
    for cross in [[0, 4, 8], [2, 4, 6]]:
        if board[cross[0]] == board[cross[1]] == board[cross[2]]:
            return board[cross[0]]

    return " "


def check_winner():
    cell = check_consecutives()
    if cell == player or cell == bot:
        return f"{cell} is the Winner!"
    else:
        return " "


def bots_move():
    if board_not_occupied():
        pos = get_random_pos()
        while board[pos-1] != " ":
            pos = get_random_pos()
        board[pos-1] = "O"


def play_move(pos):
    if empty_cell(board[pos-1]):
        board[pos-1] = "X"
        return " "
    else:
        return f"The position {pos} is occupied"


def process_user_input(user_input, isValid):
    if isValid == 1:
        return play_move(int(user_input))
    elif isValid == 0:
        print("Thanks for playing. Good Bye!")
        exit()
    else:
        return "Wrong Input. Try again"


def play_game():
    while True:
        print_instructions()
        show_board()
        if board_not_occupied():
            user_input = input("Your move: ")
            print("\n")
            user_move = process_user_input(
                user_input, validate_user_input(user_input))
            if not user_move.isspace():
                print(user_move)
            else:
                winner = check_winner()
                if winner.isspace():
                    bots_move()
                winner = check_winner()
                if not winner.isspace():
                    print(f"{winner}\n")
                    show_board()
                    reset_board()
                    print("\nLet's play again !")
        else:
            print("\n")
            print("It's a draw. Let's start again.")
            reset_board()


if __name__ == "__main__":
    reset_board()
    play_game()
