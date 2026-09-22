# What it does: Reads the pixel value at a given coordinate of an image
# Wiring:       No wiring needed (reads lenna.jpg from the current directory)
# Expected output: The pixel value at (315, 309) is printed, 315 is vertical, 309 is horizontal
# Tested on:    WalnutPi 2B / WalnutPi CM2
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_2/opencv/operate

import cv2

img = cv2.imread("lenna.jpg")   # Read lenna.jpg from the current directory

p = img[315, 309]   # Read the pixel at (315, 309), 315 is vertical, 309 is horizontal

print(p)   # Print the pixel value
