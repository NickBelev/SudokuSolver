# Sudoku Solver

A terminal-based Sudoku solving program that visualizes the solving process step-by-step. It supports dynamically loading Sudoku grids from a file and uses a backtracking algorithm to find the solution while displaying progress in real-time.

## Features
- **Dynamic Sudoku Grid Loading**: Choose from up to 50 preloaded Sudoku grids.
- **Real-Time Visualization**: Watch the solving process unfold step by step.
- **Color-Coded Display**:
  - **Cyan**: Static (given) values.
  - **Green**: Current position being solved.
  - **Yellow**: Number being experimented on.
  - **Red**: Empty cells (represented as `_`).

## Prerequisites
- Python 3.7+
- The `colorama` library for color-coded terminal output. Install it using:
  ```bash
  pip install colorama
  ```

## Usage

1. Clone the repository and navigate to the project directory:
   ```bash
   git clone https://github.com/NickBelev/SudokuSolver
   cd SudokuSolver
   ```

2. Ensure you have a file named `sudoku.txt` in the project directory, formatted as follows:
   ```
   Grid 01
   003020600
   900305001
   001806400
   008102900
   700000008
   006708200
   002609500
   800203009
   005010300

   Grid 02
   200080300
   060070084
   030500209
   000105408
   000000000
   402706000
   301007040
   720040060
   004010003
   ```

3. Run the program:
   ```bash
   python solver.py
   ```

4. Enter the grid number you wish to solve (e.g., `1` for `Grid 01`).

5. Watch the solving process unfold in the terminal. The program will display:
   - The **initial grid**.
   - The **solving process**.
   - The **solved grid** (if solvable).

6. If no solution exists for the selected grid, the program will notify you.

## How It Works
- **Grid Selection**: The program reads `sudoku.txt`, identifies the selected grid by its header (e.g., `Grid 01`), and converts it into a 2D array.
- **Backtracking Algorithm**: A recursive backtracking algorithm attempts to solve the grid by:
  1. Finding the first empty cell.
  2. Trying numbers 1–9 and checking if they satisfy Sudoku rules.
  3. Backtracking when a number leads to an invalid state.
- **Visualization**: The terminal is updated dynamically to show the grid's state during each step of the solving process.

## Example Output
```
====== Initial Board ======
7  8  _  4  _  _  1  2  _
6  _  _  _  7  5  _  _  9
_  _  _  6  _  1  _  7  8
- - - - - - - - - - - - - -
_  _  7  _  4  _  2  6  _
_  _  1  _  5  _  9  3  _
9  _  4  _  6  _  _  _  5
- - - - - - - - - - - - - -
_  7  _  3  _  _  _  1  2
1  2  _  _  _  7  4  _  _
_  4  9  2  _  6  _  _  7

...

====== Solved Board ======
4  8  3   | 9  2  1   | 6  5  7
9  6  7   | 3  4  5   | 8  2  1
2  5  1   | 8  7  6   | 4  9  3
- - - - - - - - - - - - - - - -
5  4  8   | 1  3  2   | 9  7  6
7  2  9   | 5  6  4   | 1  3  8
1  3  6   | 7  9  8   | 2  4  5
- - - - - - - - - - - - - - - -
3  7  2   | 6  8  9   | 5  1  4
8  1  4   | 2  5  3   | 7  6  9
6  9  5   | 4  1  7   | 3  8  2

```
The program updates the terminal with color-coded progress until the board is solved or deemed unsolvable.

