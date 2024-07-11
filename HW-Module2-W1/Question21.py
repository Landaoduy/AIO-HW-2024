import pandas as pd
import numpy as np

df = pd.read_csv(
    r'C:\Users\Lan Dao\Desktop\AIO-exercise\AIO-HW-2024\HW-Module2-W1\advertising.csv')

data = df.to_numpy()  # chuyển đổi từ pandas -> numpy

mean_value = df['Sales'].mean()

A = df['Sales'].iloc[(df['Sales'] - mean_value).abs().argsort().values[0]]

scores = df['Sales'].apply(lambda x: 'Good' if x > A else (
    'Bad' if x < A else 'Average'))

print(scores[7:10])
