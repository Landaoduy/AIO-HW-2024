import pandas as pd
import numpy as np

df = pd.read_csv(
    r'C:\Users\Lan Dao\Desktop\AIO-exercise\AIO-HW-2024\HW-Module2-W1\advertising.csv')

data = df.to_numpy()  # chuyển đổi từ pandas -> numpy

count = 0

for i in df['Sales']:
    if i >= 20:
        count += 1

print('Number of sales larger or equal than 20:', count)
