# Question 14: Chuyển ảnh màu sang xám dựa vào Luminosity

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

img = mpimg.imread(
    r'C:\Users\Lan Dao\Desktop\AIO-exercise\AIO-HW-2024\HW-Module2-W1\dog.jpeg')


def color2grayscale(vector):
    return vector[0]*0.21 + vector[1]*0.72 + vector[2]*0.07


gray_img_03 = np.apply_along_axis(color2grayscale, axis=2, arr=img)

print(gray_img_03[0, 0])

# plt.imshow(gray_img_03, cmap=plt.get_cmap('gray'))

# plt.show()
