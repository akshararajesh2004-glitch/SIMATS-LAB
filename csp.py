def print_grid(grid):
    for row in grid:
        print(row)
    print()

# Check if number is safe to place
def is_safe(grid, row, col, num):
    # Row and column check
    for i in range(9):
        if grid[row][i] == num or grid[i][col] == num:
            return False
    # 3x3 block check
    start_row, start_col = 3*(row//3), 3*(col//3)
    for i in range(3):
        for j in range(3):
            if grid[start_row+i][start_col+j] == num:
                return False
    return True

# CSP backtracking solver
def sudoku_solver(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1,10):
                    if is_safe(grid, row, col, num):
                        grid[row][col] = num
                        if sudoku_solver(grid):
                            return True
                        grid[row][col] = 0
                return False
    return True

# Example Sudoku puzzle (0 = empty)
grid = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

if sudoku_solver(grid):
    print("Sudoku Solved:")
    print_grid(grid)
else:
    print("No solution exists")
