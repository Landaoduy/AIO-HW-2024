
import numpy as np

import cv2

# Resize các ảnh đầu vào về cùng kích thước:

bg1_image = cv2.imread(
    r'C:\Users\Lan Dao\Desktop\AIO-exercise\AIO-HW-2024\HW-Module2-Week2\GreenBackground.png', 1)
bg1_image = cv2.resize(bg1_image, (678, 381))

ob_image = cv2.imread(
    r'C:\Users\Lan Dao\Desktop\AIO-exercise\AIO-HW-2024\HW-Module2-Week2\Object.png', 1)
ob_image = cv2.resize(ob_image, (678, 381))

bg2_image = cv2.imread(
    r'C:\Users\Lan Dao\Desktop\AIO-exercise\AIO-HW-2024\HW-Module2-Week2\NewBackground.jpg', 1)
bg2_image = cv2.resize(bg2_image, (678, 381))

# Xây dựng hàm compute_difference():


def compute_difference(bg_img, input_img):
    difference_three_channel = cv2.absdiff(bg_img, input_img)
    difference_single_channel = np.sum(difference_three_channel, axis=2) / 3.0
    difference_single_channel = difference_single_channel.astype('uint8')

    return difference_single_channel


difference_single_channel = compute_difference(bg1_image, ob_image)

# cv2.imshow('Image', difference_single_channel)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# Xây dựng hàm compute binary mask


def compute_binary_mask(difference_single_channel):
    difference_binary = np.where(difference_single_channel >= 15, 255, 0)
    difference_binary = np.stack((difference_binary,)*3, axis=-1)

    return difference_binary


binary_mask = compute_binary_mask(difference_single_channel)

# Xây dựng hàm replace background


def replace_background(bg1_image, bg2_image, ob_image):

    difference_single_channel = compute_difference(bg1_image, ob_image)

    binary_mask = compute_binary_mask(difference_single_channel)

    output = np.where(binary_mask == 255, ob_image, bg2_image)

    return output


output_image = replace_background(bg1_image, bg2_image, ob_image)

cv2.imshow('Output', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
