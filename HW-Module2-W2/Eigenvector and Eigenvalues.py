import numpy as np


def compute_eigenvalues_eigenvectors(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(
        matrix)  # tính eigenvalues và eigenvectors

    # truy cập các phần tử trong các cột của matrix
    for i in range(eigenvectors.shape[1]):

        eigenvectors[:, i] = eigenvectors[:, i] / \
            np.linalg.norm(eigenvectors[:, i])  # normalize vectors

    return eigenvalues, eigenvectors


matrix = np.array([[0.9, 0.2], [0.1, 0.8]])

eigenvalues, eigenvectors = compute_eigenvalues_eigenvectors(matrix)

print('Eigenvalues: \n', eigenvalues)

print('Eigenvectors: \n', eigenvectors)
