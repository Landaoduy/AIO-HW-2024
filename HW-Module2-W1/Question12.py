# Question 12: Chuyển ảnh màu sang xám dựa vào Lightness

import numpy as np

import matplotlib.image as mpimg

img = mpimg.imread(
    r'C:\Users\Lan Dao\Desktop\AIO-exercise\AIO-HW-2024\HW-Module2-W1\dog.jpeg')

gray_img_01 = np.zeros((img.shape[0], img.shape[1]))

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        R, G, B = img[i, j][:3]

        gray_img_01[i, j] = (max(R, G, B) + min(R, G, B))/2

print(gray_img_01[0, 0])
