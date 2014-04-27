def set_to_zero(matrix):
    """ If an element in an MxN matrix is 0, its entire row and colum is
    set to 0 """
    rows = len(matrix) 
    cols = len(matrix[0])

    out_matrix = rows * [cols * [None]]

    for row in range(rows):
        for col in range(cols):

            if matrix[row][col] == 0:

                # Set row to zero
                out_matrix[row] = cols * [0]

                # Set column to zero
                for cur_row in range(row + 1, rows):
                    out_matrix[cur_row][col] = 0
            elif out_matrix[row][col] is None:
                out_matrix[row][col] = matrix[row][col]

    return out_matrix

if __name__ == "__main__":
    matrix = [[1, 0, 1, 1],
              [1, 0, 0, 0],
              [1, 1, 1, 0],
              [1, 1, 1, 1],
              [1, 0, 1, 0]]

    print matrix
    print set_to_zero(matrix)
