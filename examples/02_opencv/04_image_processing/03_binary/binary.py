# What it does: Converts an image to grayscale and thresholds it into a binary image
# Wiring:       No wiring needed (reads lenna.jpg from the current directory)
# Expected output: The grayscale image and the binary image are shown
# Tested on:    WalnutPi 2B / WalnutPi CM2
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_2/opencv/process/binary

import cv2

img = cv2.imread("lenna.jpg", 0)   # Read lenna.jpg and convert it to grayscale
cv2.imshow('lenna', img)           # Show the image

# Threshold the image into a binary image
retval, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('binary', img)          # Show the image

cv2.waitKey()                   # Wait for any key press
cv2.destroyAllWindows()         # Close the window
