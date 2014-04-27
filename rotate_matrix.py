def rotate_matrix(matrix):
    """ Given an image represented by an NxN matrix, where each pixel in
    the image is 4 bytes, the method rotates the image by 90 degrees in
    place. """

    rows = len(matrix)

    if rows != len(matrix[0]):
        raise RuntimeError("Matrix is not N x N")

    for layer in range(0, rows/2):
 
        end = rows - layer - 1
 
        for i in range(layer, end):

            first = matrix[layer][i]
            offset = i - layer
            
            # Left -> Top
            matrix[layer][layer + offset] = matrix[end - offset][layer]

            # Bottom -> Left
            matrix[end - offset][layer] = matrix[end][end - offset]

            # Right -> Bottom
            matrix[end][end - offset] = matrix[layer + offset][end]

            # Top -> Right
            matrix[layer + offset][end] = first

    return matrix

if __name__ == "__main__":
    matrix = [[0, 1, 2, 3],
              [4, 5, 6, 7],
              [8, 9, 10, 11],
              [12, 13, 14, 15]]
    
    print matrix
    print rotate_matrix(matrix)
