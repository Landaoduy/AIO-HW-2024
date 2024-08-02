# Question 4:

import numpy as np


def compute_correlation_coefficient(X, Y):
    N = len(X)

    n1 = (N*np.sum(X*Y))

    n2 = (np.sum(X)) * (np.sum(Y))

    d1 = np.sqrt((N*np.sum(X**2)) - ((np.sum(X))**2))

    d2 = np.sqrt(((N*np.sum(Y**2)) - ((np.sum(Y))**2)))

    denominator = d1 * d2

    numerator = n1 - n2

    result = numerator / denominator

    return np.round(result, 2)


X = np.array([-2, -5, -11, 6, 4, 15, 9])
Y = np.array([4, 25, 121, 36, 16, 225, 81])

print('Correlation: ', compute_correlation_coefficient(X, Y))
