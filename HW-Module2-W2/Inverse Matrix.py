# e. Ma trận nghịch đảo

import numpy as np


def inverse_matrix(matrix):

    determinant = np.linalg.det(matrix)  # tính determinant

    if determinant == 0:
        return None

    result = np.linalg.inv(matrix)  # tính ma trận nghịch đảo

    return result


matrix = np.array([[-2, 6], [8, -4]])

print(inverse_matrix(matrix))
