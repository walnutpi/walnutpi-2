# What it does: Detects the contours of a photo
# Wiring:       No wiring needed (reads lenna.jpg from the current directory)
# Expected output: The original, grayscale, binary and contour images are shown
# Tested on:    WalnutPi 2B / WalnutPi CM2
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_2/opencv/detection/contour_detection

import cv2

img0 = cv2.imread('lenna.jpg')    # Read the image, used as the original
cv2.imshow('lenna', img0)         # Show the image

img = cv2.imread('lenna.jpg', 0)  # Read the grayscale image
cv2.imshow('gray', img)           # Show the image

# Convert the grayscale image to a binary image
t, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('binary', img)         # Show the image

# Detect the contours
contours, hierarchy = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

# Draw the contours on the original image img0
img = cv2.drawContours(img0, contours, -1, (0, 255, 0), 5)
cv2.imshow('contours', img)       # Show the image

cv2.waitKey()                   # Wait for any key press
cv2.destroyAllWindows()         # Close the window
