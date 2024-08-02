import numpy as np

# a. Độ dài vector


def compute_vector_len(vector):
    sum = 0

    for i in vector:
        sum += i**2

    return np.sqrt(sum)


vector = np.array([-2, 4, 9, 21])

print(compute_vector_len(vector))
