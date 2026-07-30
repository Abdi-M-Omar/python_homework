# --------------------------------------------------
# Task 6: More on Classes
# --------------------------------------------------


# Create a custom exception for invalid Tic-Tac-Toe moves.
class TictactoeException(Exception):

    def __init__(self, message):
        self.message = message
        super().__init__(message)


# Represent and manage a Tic-Tac-Toe board.
class Board:

    # Valid move names, arranged in board order.
    valid_moves = [
        "upper left",
        "upper center",
        "upper right",
        "middle left",
        "center",
        "middle right",
        "lower left",
        "lower center",
        "lower right",
    ]

    def __init__(self):
        # Create an empty 3-by-3 board.
        self.board_array = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "],
        ]

        # X always moves first.
        self.turn = "X"

        # Store the most recent move.
        self.last_move = None

    # Convert the board into a printable string.
    def __str__(self):
        lines = []

        lines.append(
            f" {self.board_array[0][0]} | "
            f"{self.board_array[0][1]} | "
            f"{self.board_array[0][2]}\n"
        )
        lines.append("-----------\n")

        lines.append(
            f" {self.board_array[1][0]} | "
            f"{self.board_array[1][1]} | "
            f"{self.board_array[1][2]}\n"
        )
        lines.append("-----------\n")

        lines.append(
            f" {self.board_array[2][0]} | "
            f"{self.board_array[2][1]} | "
            f"{self.board_array[2][2]}\n"
        )

        return "".join(lines)

    # Place the current player's mark on the board.
    def move(self, move_string):
        if move_string not in Board.valid_moves:
            raise TictactoeException("That's not a valid move.")

        move_index = Board.valid_moves.index(move_string)

        row = move_index // 3
        column = move_index % 3

        if self.board_array[row][column] != " ":
            raise TictactoeException("That spot is taken.")

        # Save the player who is making this move.
        current_player = self.turn

        self.board_array[row][column] = current_player
        self.last_move = move_string

        # Switch turns.
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"

    # Check whether someone won, the board is full,
    # or the game should continue.
    def whats_next(self):
        winning_lines = [
            # Rows
            [self.board_array[0][0], self.board_array[0][1], self.board_array[0][2]],
            [self.board_array[1][0], self.board_array[1][1], self.board_array[1][2]],
            [self.board_array[2][0], self.board_array[2][1], self.board_array[2][2]],

            # Columns
            [self.board_array[0][0], self.board_array[1][0], self.board_array[2][0]],
            [self.board_array[0][1], self.board_array[1][1], self.board_array[2][1]],
            [self.board_array[0][2], self.board_array[1][2], self.board_array[2][2]],

            # Diagonals
            [self.board_array[0][0], self.board_array[1][1], self.board_array[2][2]],
            [self.board_array[0][2], self.board_array[1][1], self.board_array[2][0]],
        ]

        for line in winning_lines:
            if line == ["X", "X", "X"]:
                return True, "X has won"

            if line == ["O", "O", "O"]:
                return True, "O has won"

        # Check whether every board position is filled.
        board_is_full = all(
            space != " "
            for row in self.board_array
            for space in row
        )

        if board_is_full:
            return True, "Cat's Game"

        return False, f"{self.turn}'s turn"


# --------------------------------------------------
# Main game
# --------------------------------------------------

board = Board()

print("Valid moves:")
print(", ".join(Board.valid_moves))
print()
print(board)

game_over = False

while not game_over:
    move_string = input(f"{board.turn}'s turn. Enter a move: ").strip().lower()

    try:
        board.move(move_string)
        print()
        print(board)

        game_over, message = board.whats_next()
        print(message)

    except TictactoeException as error:
        print(error.message)