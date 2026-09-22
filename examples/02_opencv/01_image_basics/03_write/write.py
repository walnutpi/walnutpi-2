# What it does: Reads an image and saves it under a new name
# Wiring:       No wiring needed (reads lenna.jpg from the current directory)
# Expected output: A new file lenna2.jpg is created in the current directory
# Tested on:    WalnutPi 2B / WalnutPi CM2
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_2/opencv/image

import cv2

img = cv2.imread("lenna.jpg")       # Read lenna.jpg from the current directory

cv2.imwrite('lenna2.jpg', img)      # Save the image as lenna2.jpg
