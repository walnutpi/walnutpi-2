# What it does: Prints the shape, size and dtype of a color image and a grayscale image
# Wiring:       No wiring needed (reads lenna.jpg from the current directory)
# Expected output: The attributes of the color image and the grayscale image are printed
# Tested on:    WalnutPi 2B / WalnutPi CM2
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_2/opencv/image

import cv2

# Read lenna.jpg in color mode
img = cv2.imread("lenna.jpg")
print('Color image: ')
print('shape: ', img.shape)
print('size: ', img.size)
print('dtype: ', img.dtype)

# Read lenna.jpg and convert it to grayscale
img = cv2.imread("lenna.jpg", 0)
print('Grayscale image: ')
print('shape: ', img.shape)
print('size: ', img.size)
print('dtype: ', img.dtype)
