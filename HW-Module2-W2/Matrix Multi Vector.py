import numpy as np

# c. Nhân vector với ma trận


def matrix_multi_vector(matrix, vector):

    result = np.dot(matrix, vector)
    return result


matrix = np.array([[-1, 1, 1], [0, -4, 9]])

vector = np.array([0, 2, 1])

print(matrix_multi_vector(matrix, vector))
