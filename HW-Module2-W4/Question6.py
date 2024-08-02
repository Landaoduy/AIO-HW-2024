import pandas as pd
import numpy as np

from Question5 import correlation

data = pd.read_csv(
    r'C:\Users\Lan Dao\Desktop\AIO-exercise\AIO-HW-2024\HW-Module2-W4\advertising.csv')

# Question 6:

features = ['TV', 'Radio', 'Newspaper']

for feature_1 in features:
    for feature_2 in features:
        correlation_value = correlation(data[feature_1], data[feature_2])

        print(f"Correlation between {feature_1} and {
              feature_2}: {round(correlation_value, 2)}")
