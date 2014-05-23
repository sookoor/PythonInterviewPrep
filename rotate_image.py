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

def rotate_image(image):
    N = len(image)
    end = N - 1
    for layer in range(0, N/2):
        for i in range(layer, N - layer - 1):
            temp = image[layer][i]
            image[layer][i] = image[end - i][layer]
            image[end - i][layer] = image[end - layer][end - i]
            image[end - layer][end - i] = image[i][end - layer]
            image[i][end - layer] = temp
    return image


if __name__ == "__main__":
    matrix = [[0, 1, 2, 3],
              [4, 5, 6, 7],
              [8, 9, 10, 11],
              [12, 13, 14, 15]]
    
    print matrix
    rotated_matrix = rotate_matrix(matrix)
    rotated_image = rotate_image(matrix)

    print rotated_matrix
    print rotated_image
 
    assert rotated_matrix  == rotated_image 
