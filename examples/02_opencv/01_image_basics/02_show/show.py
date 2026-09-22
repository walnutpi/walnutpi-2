# What it does: Displays an image file in a window
# Wiring:       No wiring needed (reads lenna.jpg from the current directory)
# Expected output: A window titled "lenna" shows the image until a key is pressed
# Tested on:    WalnutPi 2B / WalnutPi CM2
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_2/opencv/image

import cv2

img = cv2.imread("lenna.jpg")   # Read lenna.jpg from the current directory
cv2.imshow('lenna', img)        # Show the image in a window

cv2.waitKey()                   # Wait for any key press
cv2.destroyAllWindows()         # Close the window
