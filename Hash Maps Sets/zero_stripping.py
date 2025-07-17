def zero_striping(matrix: list[list[int]]):
    if not matrix or not matrix[0]:
        return
    
    m, n = len(matrix), len(matrix[0])

    first_row_has_zero = False
    
    for c in range(n):
        if matrix[0][c] == 0:
            first_row_has_zero = True
            break
    
    first_col_has_zero = False

    for r in range(m):
        if matrix[m][0] == 0:
            first_col_has_zero = True
            break
            