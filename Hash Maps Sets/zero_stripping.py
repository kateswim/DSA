def zero_striping(matrix: list[list[int]]):
    if not matrix or not matrix[0]:
        return
    
    m, n = len(matrix), len(matrix[0])

    first_row_has_zero = False
    for c in range(n):
        if matrix[0][c] == 0:
            first_row_has_zero = True
            break
