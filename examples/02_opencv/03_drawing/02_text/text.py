# What it does: Draws the text "WalnutPi" on a white canvas
# Wiring:       No wiring needed (draws on a generated canvas)
# Expected output: A window shows the text drawn on a 500x500 white image
# Tested on:    WalnutPi 2B / WalnutPi CM2
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_2/opencv/draw/string

import cv2
import numpy as np

# Create a 500x500 RGB888 white image
img = np.ones((500, 500, 3), np.uint8) * 255

# Draw 'WalnutPi' at (20,100), simplex font, size 2, red, thickness 2
cv2.putText(img, 'WalnutPi', (20, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)

cv2.imshow('String', img)       # Show the image

cv2.waitKey()                   # Wait for any key press
cv2.destroyAllWindows()         # Close the window
