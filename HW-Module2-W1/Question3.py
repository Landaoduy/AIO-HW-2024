import numpy as np

arr = np.arange(0, 10, 1)
print(arr[arr % 2 == 1])
