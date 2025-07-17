def zero_striping(matrix: list[list[int]]):
    if not matrix or not matrix[0]:
        return
    
    m, n = len(matrix), len(matrix[0])
    # check if first row initially contains zeros
    first_row_has_zero = False
    
    for c in range(n):
        if matrix[0][c] == 0:
            first_row_has_zero = True
            break
    # check if first column initially contains zeros
    first_col_has_zero = False

    for r in range(m):
        if matrix[r][0] == 0:
            first_col_has_zero = True
            break

    # use first row and column as markers, if element in submatrix zero - mark its correspondong row/column in first row/column
    for r in range(1, m):
        for c in range(1, n):
            if matrix[r][c] == 0:
                matrix[0][c] = 0
                matrix[r][0] = 0

    # update submatrix using the markers in the first row/column
    