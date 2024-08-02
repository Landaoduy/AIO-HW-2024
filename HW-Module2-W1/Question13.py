# Question 13: Chuyển ảnh màu sang xám dựa vào Average

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

img = mpimg.imread(
    r'C:\Users\Lan Dao\Desktop\AIO-exercise\AIO-HW-2024\HW-Module2-W1\dog.jpeg')


def color2grayscale(vector):
    return np.sum(vector) / 3


gray_img_02 = np.apply_along_axis(color2grayscale, axis=2, arr=img)

print(gray_img_02[0, 0])

# plt.imshow(gray_img_02, cmap=plt.get_cmap('gray'))

# plt.show()
