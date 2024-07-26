# 4.2) Compute function prior probability

import numpy as np

from Dataset import train_data


def compute_prior_probability(train_data):
    y_unique = ['no', 'yes']

    prior_probability = np.zeros(len(y_unique))

    for i in range(0, len(y_unique)):

        prior_probability[i] = len(
            np.where(train_data[:, 4] == y_unique[i])[0]) / len(train_data)
        # tạo mảng để xem giá trị cột thứ 5
        # trả về các chỉ số của các phần tử trong train_data[:, 4] mà có giá trị bằng với y_unique[i]

    return prior_probability


# Question 14:
prior_probability = compute_prior_probability(train_data)
print('P(Play tennis = No):', prior_probability[0])
print('P(Play tennis = Yes):', prior_probability[1])
