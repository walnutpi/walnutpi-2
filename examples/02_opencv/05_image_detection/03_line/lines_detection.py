# What it does: Detects straight lines in an image with the Hough transform
# Wiring:       No wiring needed (reads lines.png from the current directory)
# Expected output: The detected lines are printed and drawn on the original image
# Tested on:    WalnutPi 2B / WalnutPi CM2
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_2/opencv/detection/line_detection

import cv2
import numpy as np

img0 = cv2.imread('lines.png')   # Read the image
cv2.imshow('lines', img0)        # Show the original image

# Convert the color image to a single channel grayscale image
img1 = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)

# Convert the grayscale image to a binary image
t, img2 = cv2.threshold(img1, 127, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('binary', img2)       # Show the binary image

# Detect the lines
lines = cv2.HoughLinesP(img2, 1, np.pi/180, 15, 100, 20)

print(lines)   # Print the line information

# Draw the lines on the original image
for l in lines:
    x0, y0, x1, y1 = l[0]
    cv2.line(img0, (x0, y0), (x1, y1), (0, 255, 0), 3)

cv2.imshow('result', img0)      # Show the image

cv2.waitKey()                   # Wait for any key press
cv2.destroyAllWindows()         # Close the window
