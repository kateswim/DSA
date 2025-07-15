def verify_sudoku_board(board: list[list[int]]):
    row_sets = [set() for _ in range(9)]
    column_set = [set() for _ in range(9)]
    subgrid_sets = [[set() for _ in range(3)] for _ in range(3)]