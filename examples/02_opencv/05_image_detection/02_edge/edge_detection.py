# What it does: Runs Canny edge detection with two different threshold pairs
# Wiring:       No wiring needed (reads lenna.jpg from the current directory)
# Expected output: The original image and two edge images with different thresholds are shown
# Tested on:    WalnutPi 2B / WalnutPi CM2
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_2/opencv/detection/edge_detection

import cv2

img = cv2.imread('lenna.jpg')   # Read the image, used as the original
cv2.imshow('lenna', img)        # Show the original image

# Edge detection with the first threshold pair
e1 = cv2.Canny(img, 20, 60)
cv2.imshow('e1', e1)   # Show the image

# Edge detection with the second threshold pair
e2 = cv2.Canny(img, 200, 400)
cv2.imshow('e2', e2)   # Show the image

cv2.waitKey()                   # Wait for any key press
cv2.destroyAllWindows()         # Close the window
