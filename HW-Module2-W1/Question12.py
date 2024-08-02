# Question 12: Chuyển ảnh màu sang xám dựa vào Lightness


import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

img = mpimg.imread(
    r'C:\Users\Lan Dao\Desktop\AIO-exercise\AIO-HW-2024\HW-Module2-W1\dog.jpeg')


def color2grayscale(vector):
    return np.max(vector)*0.5 + np.min(vector)*0.5


gray_img_01 = np.apply_along_axis(color2grayscale, axis=2, arr=img)

print(gray_img_01[0, 0])

# plt.imshow(gray_img_01, cmap=plt.get_cmap('gray'))

# plt.show()
