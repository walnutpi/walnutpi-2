# What it does: Flips an image along the X axis, the Y axis and both axes
# Wiring:       No wiring needed (reads lenna.jpg from the current directory)
# Expected output: The original image and three flipped versions are shown
# Tested on:    WalnutPi 2B / WalnutPi CM2
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_2/opencv/process/flip

import cv2

img = cv2.imread("lenna.jpg")   # Read lenna.jpg from the current directory
cv2.imshow('lenna', img)        # Show the image

img1 = cv2.flip(img, 0)         # Flip along the X axis
cv2.imshow('X', img1)           # Show the image

img2 = cv2.flip(img, 1)         # Flip along the Y axis
cv2.imshow('Y', img2)           # Show the image

img3 = cv2.flip(img, -1)        # Flip along both the X and Y axes
cv2.imshow('X & Y', img3)       # Show the image

cv2.waitKey()                   # Wait for any key press
cv2.destroyAllWindows()         # Close the window
