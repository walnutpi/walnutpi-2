# What it does: Reads an image file and prints its pixel data
# Wiring:       No wiring needed (reads lenna.jpg from the current directory)
# Expected output: The image array of lenna.jpg is printed to the terminal
# Tested on:    WalnutPi 2B / WalnutPi CM2
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_2/opencv/image

import cv2

img = cv2.imread("lenna.jpg")   # Read lenna.jpg from the current directory

print(img)   # Print the image information
