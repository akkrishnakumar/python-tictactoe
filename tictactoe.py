# Tic Tac Toe - Python #

def init_game():
    return list(
        map(
            lambda pos: " ",
            list(range(0, 9))
        )
    )


board = init_game()


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


def play_move(pos):
    board[pos-1] = "X"


def play_game():
    while True:
        print_instructions()
        show_game()
        user_input = input("Your move: ")
        isValid = validate_user_input(user_input)
        if isValid == 1:
            play_move(int(user_input))
        elif isValid == 0:
            exit()
        else:
            print("Wrong Input. Try again")
            pass


init_game()
play_game()
