"""Given an image represented by an NxN matrix, where each pixel in the image is an integer from 0 to 9, write a 
function rotate_image that receives a matrix as input and rotates the image by 90 degrees in 
the counter-clockwise direction."""

"""
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
"""
line = range(10)
matrix = [[*line] for x in range(10)]
# matrix[4][5] = 5
# temp = []


def rotate_image(matrix):
    for x in range(len(matrix)//2):
        for y in range(len(matrix[x])-1-(2*x)):
            # temp=(matrix[len(matrix)-(x+1)][x])
            matrix[x][y+x] = '*'+str(matrix[x][x+y])
    return matrix


# for x in matrix:
#     print(x)
tots = ""
after = rotate_image(matrix)
for x in range(len(after)):
    for y in range(len(after[x])):
        if str(after[x][y])[0] == '*':
            tots += after[x][y]
        else:
            tots += ' '+str(after[x][y])
    print(tots)
    tots = ''
