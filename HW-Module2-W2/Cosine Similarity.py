import numpy as np


def compute_cosine(v1, v2):

    product_v1_v2 = np.dot(v1, v2)

    sum_of_squares_v1 = np.sum(v1**2)
    length_of_v1 = np.sqrt(sum_of_squares_v1)

    sum_of_squares_v2 = np.sum(v2**2)
    length_of_v2 = np.sqrt(sum_of_squares_v2)

    product_length = length_of_v1 * length_of_v2

    cos_sim = product_v1_v2 / product_length

    return cos_sim


v1 = np.array([1, 2, 3, 4])

v2 = np.array([1, 0, 3, 0])

print(compute_cosine(v1, v2))
