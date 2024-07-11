import pandas as pd
import numpy as np

df = pd.read_csv(
    r'C:\Users\Lan Dao\Desktop\AIO-exercise\AIO-HW-2024\HW-Module2-W1\advertising.csv')

data = df.to_numpy()  # chuyển đổi từ pandas -> numpy

# Question 19:

average_newspaper = df['Newspaper'].mean()

filtered_df_1 = df[df['Newspaper'] > average_newspaper]

sum_sales = filtered_df_1['Sales'].sum()

print('Sum of sales with Newspaper > average:', sum_sales)
