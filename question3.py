# Question 3

import random
import math


def calculate_loss(num_samples, loss_name):
    if not num_samples.isnumeric():
        print('number of samples must be an integer number')
        return

    num_samples = int(num_samples)

    predicts = []
    targets = []

    for i in range(num_samples):
        target = random.uniform(0, 10)
        predict = random.uniform(0, 10)

        predicts.append(predict)
        targets.append(target)

    if loss_name == 'MAE':
        loss = sum(abs(targets[i] - predicts[i])
                   for i in range(num_samples)) / num_samples

    elif loss_name == 'MSE':
        loss = sum((targets[i] - predicts[i]) **
                   2 for i in range(num_samples)) / num_samples

    elif loss_name == 'RMSE':
        loss = math.sqrt(
            sum((targets[i] - predicts[i])**2 for i in range(num_samples))) / num_samples

    else:
        print("Invalid loss name")

    for i in range(num_samples):
        print(
            f"Loss name: {loss_name}, Sample: {i}, Pred: {predicts[i]}, Target: {targets[i]}")

    print(f"Loss: {loss}")
