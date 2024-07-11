import pandas as pd
import numpy as np

df = pd.read_csv(
    r'C:\Users\Lan Dao\Desktop\AIO-exercise\AIO-HW-2024\HW-Module2-W1\advertising.csv')

data = df.to_numpy()  # chuyển đổi từ pandas -> numpy

# Question 18:

filtered_df = df[df['Sales'] >= 15]  # Xét các giá trị của Sales

average_radio = filtered_df['Radio'].mean()

print('Average radio with Sales >= 15:', average_radio)
