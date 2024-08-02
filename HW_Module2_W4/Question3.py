# Question 3:

from Question1 import compute_mean
import numpy as np


def compute_std(X):
    mean = compute_mean(X)
    variance = 0
    length = len(X)

    for i in range(length):
        variance += (X[i] - mean) ** 2

    variance = variance / length
    std = np.sqrt(variance)

    return std


X = [171, 176, 155, 167, 169, 182]

print('Standard Deviation:', compute_std(X))
