# Question 2:

import math


def is_number(n):
    try:
        float(n)
        return True

    except ValueError:
        return False


def sigmoid(n):

    sigmoid = 1 / (1 + math.exp(-n))
    print(f"The value of sigmoid is: {sigmoid}")


def reLu_function(n):

    if n <= 0:

        return 0

    else:
        return n


def ELU_function(n, alpha):

    if n <= 0:
        elu_func = alpha * (math.exp(n)-1)
        return (f"The value of ELU is: {elu_func}")

    else:
        return n
