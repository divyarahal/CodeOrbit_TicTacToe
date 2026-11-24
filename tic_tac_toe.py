"""
Tic-Tac-Toe: Human vs Computer (Minimax AI)

- You play 'X', the computer plays 'O'.
- The board is printed after every move.
- Detects win, loss and draw.
- The AI uses the Minimax algorithm, so it never loses
  (the best you can do against it is a draw).
"""

WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),   # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),   # columns
    (0, 4, 8), (2, 4, 6),              # diagonals
]

HUMAN = "X"
COMPUTER = "O"


def print_board(board):
    """Display the board; empty cells show their position number (1-9)."""
    cells = [board[i] if board[i] != " " else str(i + 1) for i in range(9)]
    print()
    print(f" {cells[0]} | {cells[1]} | {cells[2]} ")
    print("---+---+---")
    print(f" {cells[3]} | {cells[4]} | {cells[5]} ")
    print("---+---+---")
    print(f" {cells[6]} | {cells[7]} | {cells[8]} ")
    print()


def check_winner(board):
    """Return 'X' or 'O' if someone has won, otherwise None."""
    for a, b, c in WIN_LINES:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    return None


def is_full(board):
    return " " not in board


def available_moves(board):
    return [i for i in range(9) if board[i] == " "]


def minimax(board, is_computer_turn, depth):
    """
    Score a position from the computer's point of view.
      +10 - depth : computer wins (faster wins score higher)
      depth - 10  : human wins   (slower losses score higher)
      0           : draw
    """
    winner = check_winner(board)
    if winner == COMPUTER:
        return 10 - depth
    if winner == HUMAN:
        return depth - 10
    if is_full(board):
        return 0

    if is_computer_turn:
        best = -float("inf")
        for move in available_moves(board):
            board[move] = COMPUTER
            best = max(best, minimax(board, False, depth + 1))
            board[move] = " "
        return best
    else:
        best = float("inf")
        for move in available_moves(board):
            board[move] = HUMAN
            best = min(best, minimax(board, True, depth + 1))
            board[move] = " "
        return best


def computer_move(board):
    """Pick the move with the highest Minimax score."""
    best_score = -float("inf")
    best_move = None
    for move in available_moves(board):
        board[move] = COMPUTER
        score = minimax(board, False, 1)
        board[move] = " "
        if score > best_score:
            best_score = score
            best_move = move
    return best_move


def human_move(board):
    """Ask the user for a valid move (1-9)."""
    while True:
        choice = input("Your move (1-9): ").strip()
        if not choice.isdigit() or not 1 <= int(choice) <= 9:
            print("Invalid input. Enter a number from 1 to 9.")
            continue
        index = int(choice) - 1
        if board[index] != " ":
            print("That cell is already taken. Try another one.")
            continue
        return index


def play_game():
    board = [" "] * 9
    print("=== TIC-TAC-TOE ===")
    print(f"You are '{HUMAN}', the computer is '{COMPUTER}'.")

    first = input("Do you want to go first? (y/n): ").strip().lower()
    human_turn = first != "n"

    print_board(board)

    while True:
        if human_turn:
            board[human_move(board)] = HUMAN
        else:
            move = computer_move(board)
            board[move] = COMPUTER
            print(f"Computer plays position {move + 1}.")

        print_board(board)

        winner = check_winner(board)
        if winner == HUMAN:
            print("You win! 🎉")
            break
        if winner == COMPUTER:
            print("Computer wins. You lose!")
            break
        if is_full(board):
            print("It's a draw!")
            break

        human_turn = not human_turn


def main():
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break
        print()


if __name__ == "__main__":
    main()
