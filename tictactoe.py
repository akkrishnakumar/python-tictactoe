# Tic Tac Toe - Python #
import random


class TicTacToe():

    board = []

    player = "X"
    bot = "O"

    def __init__(self):
        print("Welcome to Tic Tac Toe")
        self.choose_marker(input("Choose you marker (X/O): "))
        self.reset_board()

    def play(self):
        while True:
            self.print_instructions()
            self.show_board()
            if self.board_has_free_cells():
                user_input = input("Your move: ")
                print("\n")
                user_move = self.process_user_input(
                    user_input,
                    self.validate_user_input(user_input)
                )
                if not user_move.isspace():
                    print(user_move)
                else:
                    winner = self.check_winner()
                    if winner.isspace():
                        self.bots_move()
                    winner = self.check_winner()
                    if not winner.isspace():
                        self.show_board()
                        print(f"{winner}\n")
                        self.reset_board()
                        print("\nLet's play again !")
            else:
                print("\n")
                print("It's a draw. Let's start again.")
                self.reset_board()

    def show_board(self):
        for index, value in enumerate(self.board):
            if (index + 1) % 3 != 0:
                self.print_position(value, True)
            else:
                self.print_position(value)
                self.print_game_separator(index)
        print("")

    def process_user_input(self, user_input, isValid):
        if isValid == 1:
            return self.player_move(int(user_input))
        elif isValid == 0:
            print("Thanks for playing. Good Bye!")
            exit()
        else:
            return "Wrong Input. Try again"

    def player_move(self, pos):
        if empty_cell(self.board[pos-1]):
            self.board[pos-1] = self.player
            return " "
        else:
            return f"The position {pos} is occupied"

    def bots_move(self):
        if self.board_has_free_cells():
            pos = self.get_random_pos()
            while self.board[pos-1] != " ":
                pos = self.get_random_pos()
            self.board[pos-1] = self.bot

    def check_winner(self):
        cell = self.check_consecutives()
        if cell == self.player or cell == self.bot:
            return f"{cell} is the Winner!"
        else:
            return " "

    def check_consecutives(self):
        # TODO: Akhil - Need to improve the logic here

        # horizontal
        for row in [0, 3, 6]:
            curr = self.board[row]
            if curr == self.board[row+1] and curr == self.board[row+2] and not empty_cell(curr):
                return curr

        # vertical
        for col in [0, 1, 2]:
            curr = self.board[col]
            if curr == self.board[col+3] and curr == self.board[col+6] and not empty_cell(curr):
                return curr

        # cross
        for cross in [[0, 4, 8], [2, 4, 6]]:
            if self.board[cross[0]] == self.board[cross[1]] == self.board[cross[2]]:
                return self.board[cross[0]]

        return " "

    def validate_user_input(self, user_input):
        if user_input.isdigit() and int(user_input) in range(1, 10):
            return 1
        elif user_input.isalpha() and user_input == 'q':
            return 0
        else:
            return -1

    def choose_marker(self, marker):
        if marker.upper() == "X" or marker.upper() == "O":
            print(f"You have chosen '{marker.upper()}'")
            self.player = marker.upper()
            self.bot = opposite(marker)
        else:
            print("You choice is weird. Defaulting to 'X'")

    def print_position(self, value, separator=False):
        if separator:
            print(f" {value} ", end="|")
        else:
            print(f" {value} ", end="")

    def print_game_separator(self, index):
        if index + 1 != 9:
            print("\n---|---|---")
        else:
            print("")

    def board_has_free_cells(self):
        return " " in self.board

    def reset_board(self):
        self.board = list(
            map(
                lambda pos: " ",
                list(range(0, 9))
            )
        )

    def print_instructions(self):
        self.separator()
        print("Enter position number (1-9) to play your move")
        print("Enter 'q' to exit")
        self.separator()

    def separator(self):
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

    def get_random_pos(self):
        return random.randint(1, 9)


def empty_cell(cell):
    return cell.isspace()


def opposite(marker):
    if marker.upper() == "X":
        return "O"
    else:
        return "X"
