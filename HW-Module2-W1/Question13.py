# Question 13: Chuyển ảnh màu sang xám dựa vào Average

import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread(
    r'C:\Users\Lan Dao\Desktop\AIO-exercise\AIO-HW-2024\HW-Module2-W1\dog.jpeg')

gray_img_02 = np.zeros((img.shape[0], img.shape[1]))

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        R, G, B = img[i, j][:3]

        gray_img_02[i, j] = (R+G+B)/3

print(gray_img_02[0, 0])
