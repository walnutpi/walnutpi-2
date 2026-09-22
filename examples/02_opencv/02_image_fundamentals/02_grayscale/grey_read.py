# What it does: Converts an image to grayscale and reads one of its pixels
# Wiring:       No wiring needed (reads lenna.jpg from the current directory)
# Expected output: The grayscale image is shown and the pixel value at (315, 309) is printed
# Tested on:    WalnutPi 2B / WalnutPi CM2
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_2/opencv/operate

import cv2

img = cv2.imread("lenna.jpg", 0)   # Read lenna.jpg and convert it to grayscale
cv2.imshow('grey', img)            # Show the image

p = img[315, 309]   # Read the pixel at (315, 309), 315 is vertical, 309 is horizontal
print(p)            # Print the pixel value

cv2.waitKey()                   # Wait for any key press
cv2.destroyAllWindows()         # Close the window
