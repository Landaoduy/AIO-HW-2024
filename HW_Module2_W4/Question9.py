# Question 9:

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_csv(
    r'C:\Users\Lan Dao\Desktop\AIO-exercise\AIO-HW-2024\HW_Module2_W4\advertising.csv')

data_corr = data.corr()

sns.heatmap(data_corr, annot=True, fmt=".2f", linewidth=.5)

plt.figure(figsize=(10, 8))

plt.show()
