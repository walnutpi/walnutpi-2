# What it does: Detects circles in an image with the Hough transform
# Wiring:       No wiring needed (reads circle.jpg from the current directory)
# Expected output: The detected circles are printed and drawn on the original image
# Tested on:    WalnutPi 2B / WalnutPi CM2
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_2/opencv/detection/circle_detection

import cv2
import numpy as np

img0 = cv2.imread('circle.jpg')   # Read the image

# Convert the color image to a single channel grayscale image
img1 = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)

# Detect the circles
circles = cv2.HoughCircles(img1, cv2.HOUGH_GRADIENT, 1, 50, 100, 25)

# Round all the coordinates and radii to integers
circles = np.uint(np.around(circles))

print(circles)   # Print the circle information

# Draw the circles on the original image
for c in circles[0]:
    x, y, r = c
    cv2.circle(img0, (x, y), 2, (0, 255, 0), 3)   # Draw the center
    cv2.circle(img0, (x, y), r, (0, 255, 0), 3)   # Draw the ring

cv2.imshow('result', img0)      # Show the image

cv2.waitKey()                   # Wait for any key press
cv2.destroyAllWindows()         # Close the window
