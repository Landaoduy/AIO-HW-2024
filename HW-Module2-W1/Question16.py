import pandas as pd
import numpy as np

df = pd.read_csv(
    r'C:\Users\Lan Dao\Desktop\AIO-exercise\AIO-HW-2024\HW-Module2-W1\advertising.csv')

data = df.to_numpy()  # chuyển đổi từ pandas -> numpy


mean_TV = np.mean(df['TV'])

print('Mean of TV:', mean_TV)
