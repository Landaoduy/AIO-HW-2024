import pandas as pd
import numpy as np

data = pd.read_csv(
    r'C:\Users\Lan Dao\Desktop\AIO-exercise\AIO-HW-2024\HW-Module2-W4\advertising.csv')


def correlation(x, y):

    numerator = np.sum((x - np.mean(x)) * (y - np.mean(y)))

    denominator = np.sqrt(np.sum((x - np.mean(x))**2)
                          * np.sum((y - np.mean(y))**2))

    if denominator == 0:
        return 0

    return numerator / denominator


x = data['TV']

y = data['Radio']

corr_xy = correlation(x, y)

print(corr_xy)
