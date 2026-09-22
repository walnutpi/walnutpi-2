# What it does: Detects the contours of shapes drawn on a generated canvas
# Wiring:       No wiring needed (draws on a generated canvas)
# Expected output: The color, grayscale, binary and contour images are shown
# Tested on:    WalnutPi 2B / WalnutPi CM2
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_2/opencv/detection/contour_detection

import cv2
import numpy as np

# Create a 300x300 RGB888 white image
img = np.ones((300, 300, 3), np.uint8) * 255

# Draw a blue filled circle
img0 = cv2.circle(img, (100, 100), 50, (255, 0, 0), -1)

# Draw a red filled rectangle
img = cv2.rectangle(img0, (150, 150), (250, 250), (0, 0, 255), -1)

cv2.imshow('color', img)   # Show the image

# Convert the color image to a single channel grayscale image
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', img)    # Show the image

# Convert the grayscale image to a binary image
t, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('binary', img)  # Show the image

# Detect the contours
contours, hierarchy = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

# Draw the contours on the original image img0
img = cv2.drawContours(img0, contours, -1, (0, 255, 0), 5)
cv2.imshow('contours', img)   # Show the image

cv2.waitKey()                   # Wait for any key press
cv2.destroyAllWindows()         # Close the window
