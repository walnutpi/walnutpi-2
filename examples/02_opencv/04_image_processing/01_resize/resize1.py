# What it does: Resizes an image with the dsize parameter
# Wiring:       No wiring needed (reads lenna.jpg from the current directory)
# Expected output: The original image, a 200x200 version and a 500x500 version are shown
# Tested on:    WalnutPi 2B / WalnutPi CM2
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_2/opencv/process/resize

import cv2

img = cv2.imread("lenna.jpg")   # Read lenna.jpg from the current directory
cv2.imshow('lenna', img)        # Show the image

img1 = cv2.resize(img, (200, 200))   # Resize to 200x200 with the dsize parameter
cv2.imshow('200x200', img1)          # Show the image

img2 = cv2.resize(img, (500, 500))   # Resize to 500x500 with the dsize parameter
cv2.imshow('500x500', img2)          # Show the image

cv2.waitKey()                   # Wait for any key press
cv2.destroyAllWindows()         # Close the window
