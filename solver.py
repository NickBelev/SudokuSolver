from typing import List, Tuple, Optional
from time import sleep
from colorama import Fore, Style, init

# Initialize colorama
init()

def solve(board: List[List[int]]) -> bool:
    """
    Solves the Sudoku board using backtracking while displaying the solving process.

    Args:
        board (List[List[int]]): The 9x9 Sudoku board represented as a list of lists.

    Returns:
        bool: True if the Sudoku is solvable, False otherwise.
    """
    find = find_empty(board)
    if not find:
        return True  # Puzzle is solved

    row, col = find

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num
            print_board(board, (row, col), num)
            sleep(0.01)  # Add a slight delay to simulate frames

            if solve(board):
                return True

            board[row][col] = 0  # Backtrack
            print_board(board, (row, col), 0)
            sleep(0.01)

    return False

def is_valid(board: List[List[int]], num: int, pos: Tuple[int, int]) -> bool:
    """
    Checks if a number can be placed in a given position without violating Sudoku rules.

    Args:
        board (List[List[int]]): The 9x9 Sudoku board.
        num (int): The number to be placed (1-9).
        pos (Tuple[int, int]): The (row, col) position to check.

    Returns:
        bool: True if valid, False otherwise.
    """
    row, col = pos

    # Check the row
    if num in board[row]:
        return False

    # Check the column
    if num in [board[i][col] for i in range(9)]:
        return False

    # Check the 3x3 subgrid
    box_start_row, box_start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(box_start_row, box_start_row + 3):
        for j in range(box_start_col, box_start_col + 3):
            if board[i][j] == num:
                return False

    return True

def find_empty(board: List[List[int]]) -> Optional[Tuple[int, int]]:
    """
    Finds an empty cell (represented by 0) on the Sudoku board.

    Args:
        board (List[List[int]]): The 9x9 Sudoku board.

    Returns:
        Optional[Tuple[int, int]]: The (row, col) position of the empty cell, or None if no empty cell is found.
    """
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i, j
    return None

def load_board_from_file(file_path: str, grid_choice: int) -> List[List[int]]:
    """
    Loads a Sudoku board from a file based on the user's choice.

    Args:
        file_path (str): The path to the file containing Sudoku grids.
        grid_choice (int): The grid number to load (1-based index).

    Returns:
        List[List[int]]: The 9x9 Sudoku board as a list of lists.
    """
    with open(file_path, "r") as file:
        lines = file.readlines()

    grid_header = f"Grid {grid_choice:02}"
    start_index = lines.index(grid_header + "\n") + 1

    board = []
    for i in range(9):
        row = [int(char) for char in lines[start_index + i].strip()]
        board.append(row)

    return board

def print_board(board: List[List[int]], current_pos: Optional[Tuple[int, int]] = None, current_num: int = 0, clear: bool = True) -> None:
    """
    Prints the Sudoku board in a formatted manner with color highlights.

    Args:
        board (List[List[int]]): The 9x9 Sudoku board.
        current_pos (Optional[Tuple[int, int]]): The current position being experimented upon.
        current_num (int): The number being tried at the current position.
        clear (bool): Whether to clear the terminal before printing.
    """
    if clear:
        print("\033c", end="")  # Clear the terminal for a frame-by-frame effect

    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print(Fore.WHITE + "- - - - - - - - - - - - - - - -" + Style.RESET_ALL)

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(Fore.WHITE + " | " + Style.RESET_ALL, end="")

            if board[i][j] != 0:
                color = Fore.CYAN if (i, j) != current_pos else Fore.GREEN
                print(color + str(board[i][j]) + Style.RESET_ALL, end="  " if j != 8 else "\n")
            elif (i, j) == current_pos:
                print(Fore.YELLOW + str(current_num) + Style.RESET_ALL, end="  " if j != 8 else "\n")
            else:
                print(Fore.RED + "_" + Style.RESET_ALL, end="  " if j != 8 else "\n")

if __name__ == "__main__":
    file_path = "sudoku.txt"
    choice = int(input("Enter the grid number (1-50) you want to solve: "))

    board = load_board_from_file(file_path, choice)

    print("====== Initial Board ======")
    print_board(board, clear=False)  # Do not clear terminal here
    sleep(5)

    if solve(board):
        print("\n====== Solved Board ======")
        print_board(board, clear=False)  # Do not clear terminal here
    else:
        print("\nNo solution exists for the given Sudoku board.")

