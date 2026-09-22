# What it does: Resizes an image with the fx and fy scale factors
# Wiring:       No wiring needed (reads lenna.jpg from the current directory)
# Expected output: The original image, a half size version and a double size version are shown
# Tested on:    WalnutPi 2B / WalnutPi CM2
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_2/opencv/process/resize

import cv2

img = cv2.imread("lenna.jpg")   # Read lenna.jpg from the current directory
cv2.imshow('lenna', img)        # Show the image

img1 = cv2.resize(img, None, fx=1/2, fy=1/2)   # Scale down to 1/2 with fx and fy
cv2.imshow('0.5x', img1)                       # Show the image

img2 = cv2.resize(img, None, fx=2, fy=2)       # Scale up 2x with fx and fy
cv2.imshow('2x', img2)                         # Show the image

cv2.waitKey()                   # Wait for any key press
cv2.destroyAllWindows()         # Close the window
