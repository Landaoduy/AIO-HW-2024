import pandas as pd
import numpy as np

df = pd.read_csv(
    r'C:\Users\Lan Dao\Desktop\AIO-exercise\AIO-HW-2024\HW-Module2-W1\advertising.csv')

data = df.to_numpy()  # chuyển đổi từ pandas -> numpy

# Question 15:

max_sale = np.max(df['Sales'])

index = np.argmax(df['Sales'])

print('Max sale:', max_sale)

print('Index of max scale:', index)
