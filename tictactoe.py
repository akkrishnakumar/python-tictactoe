# Tic Tac Toe - Python #
import random

board = list()


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


def show_game():
    # print(f"Board:\n{board}\n")
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


def bots_move():
    if board_not_occupied():
        pos = get_random_pos()
        while board[pos-1] != " ":
            pos = get_random_pos()
        board[pos-1] = "O"


def play_move(pos):
    if board[pos-1].isspace():
        board[pos-1] = "X"
        bots_move()
    else:
        print(f"The position {pos} is occupied")


def play_game():
    while True:
        print_instructions()
        show_game()
        if board_not_occupied():
            user_input = input("Your move: ")
            print("\n")
            isValid = validate_user_input(user_input)
            if isValid == 1:
                play_move(int(user_input))
            elif isValid == 0:
                print("Thanks for playing. Good Bye!")
                exit()
            else:
                print("Wrong Input. Try again")
                pass
        else:
            print("\n")
            print("It's a draw. Let's start again.")
            reset_board()

if __name__ == "__main__":
    reset_board()
    play_game()
