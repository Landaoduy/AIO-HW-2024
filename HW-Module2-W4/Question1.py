# Question 1:

import numpy as np


def compute_mean(X):
    mean = np.mean(X)

    return mean


X = [2, 0, 2, 2, 7, 4, -2, 5, -1, -1]
print('Mean:', compute_mean(X))
