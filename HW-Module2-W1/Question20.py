import pandas as pd
import numpy as np

df = pd.read_csv(
    r'C:\Users\Lan Dao\Desktop\AIO-exercise\AIO-HW-2024\HW-Module2-W1\advertising.csv')

data = df.to_numpy()  # chuyển đổi từ pandas -> numpy

# Question 20:

average_sales = df['Sales'].mean()

scores = df['Sales'].apply(lambda x: 'Good' if x > average_sales else (
    'Bad' if x < average_sales else 'Average'))

print(scores[7:10])
