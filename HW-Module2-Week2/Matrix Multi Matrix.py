# d. Nhân ma trận với ma trận

import numpy as np


def matrix_multi_matrix(matrix1, matrix2):

    result = np.dot(matrix1, matrix2)
    return result


matrix1 = np. array([[0, 1, 2], [2, -3, 1]])
matrix2 = np. array([[1, -3], [6, 1], [0, -1]])

print(matrix_multi_matrix(matrix1, matrix2))
