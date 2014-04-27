def set_to_zero(matrix):
    """ If an element in an MxN matrix is 0, its entire row and colum is
    set to 0 """
    rows = len(matrix) 
    cols = len(matrix[0])

    rows_to_zero = set()
    cols_to_zero = set()

    for row in range(rows):
        for col in range(cols):

            if matrix[row][col] == 0:

                # Mark to be zeroed
                rows_to_zero.add(row)
                cols_to_zero.add(col)

    for row in range(rows):
        for col in range(cols):
            if row in rows_to_zero or col in cols_to_zero:
                matrix[row][col] = 0

    return matrix

if __name__ == "__main__":
    matrix = [[1, 0, 1, 1],
              [1, 0, 0, 0],
              [1, 1, 1, 0],
              [1, 1, 1, 1],
              [1, 0, 1, 0]]

    print matrix
    print set_to_zero(matrix)
