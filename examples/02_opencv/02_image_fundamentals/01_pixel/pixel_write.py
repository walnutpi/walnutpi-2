# What it does: Modifies a block of pixels and shows the image before and after
# Wiring:       No wiring needed (reads lenna.jpg from the current directory)
# Expected output: The original image and the image with a green 30x30 block are shown
# Tested on:    WalnutPi 2B / WalnutPi CM2
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_2/opencv/operate

import cv2

img = cv2.imread("lenna.jpg")   # Read lenna.jpg from the current directory
cv2.imshow('1', img)            # Show the original image

for i in range(30):
    for j in range(30):
        img[i, j] = [0, 255, 0]   # Change the pixel to green

cv2.imshow('2', img)            # Show the modified image

cv2.waitKey()                   # Wait for any key press
cv2.destroyAllWindows()         # Close the window
