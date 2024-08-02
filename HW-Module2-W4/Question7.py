import pandas as pd
import numpy as np

data = pd.read_csv(
    r'C:\Users\Lan Dao\Desktop\AIO-exercise\AIO-HW-2024\HW-Module2-W4\advertising.csv')


x = data['Radio']

y = data['Newspaper']

result = np.corrcoef(x, y)

print(result)
