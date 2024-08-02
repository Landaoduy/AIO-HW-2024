# Question 2:

import numpy as np


def compute_median(X):
    size = len(X)
    X = np.sort(X)
    print(X)

    if size % 2 == 0:
        median = 1/2 * (X[size // 2] + X[size // 2 - 1])
    else:
        median = 1/2 * X[size // 2 + 1]

    return median


X = [1, 5, 4, 4, 9, 13]
print('Median:', compute_median(X))
