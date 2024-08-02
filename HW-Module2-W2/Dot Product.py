# b. Phép tích vô hướng

import numpy as np


def compute_dot_product(vector1, vector2):

    result = np.dot(vector1, vector2)
    return result


vector1 = np.array([0, 1, -1, 2])
vector2 = np.array([2, 5, 1, 0])

print(compute_dot_product(vector1, vector2))
