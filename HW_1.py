# Solve the following Matrix
"""
(   0   1   -1  |   -1  )
(   3   -1  1   |   4   )
(   1   1   -2  |   -3  )
"""


def gausian_elimination(matrix):
    """
    Received 2D array matrix and tries to solve it using gausian elimination
    :param matrix: 2D array of floats/ints
    :return: Solved matrix
    """
    e_width = len(matrix)
    e_height = len(matrix[0])

    e, I = i_matrix_gen(e_width, e_height)
    for i in range(e_height):
        e[i][i] = I[i][i]/matrix[i][i] # Pivot 1
        for j in range(i,e_height): # Pivot the rest of the column
            e[j][i] = -matrix[j][i]




def i_matrix_gen(e_width, e_height):
    """
    Generates I matrix
    :param e_width: Matrix columns
    :param e_height: Matrix height
    :return: I Matrix
    """
    i = 0
    I = [[0 for i in range(e_width)] for j in range(e_height)]
    while i < e_width and i < e_height:
        I[i][i] = 1
        i += 1
    return I


mat = [[0, 3, 1], [1, -1, 1], [-1, 1, -2]]
param = ['x', 'y', 'z']
sol = [-1, 4, -3]
