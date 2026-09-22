# What it does: Detects license plates in a photo with a Haar cascade classifier
# Wiring:       No wiring needed (reads car.png and data/ from the current directory)
# Expected output: The photo is shown with every detected plate boxed in red
# Tested on:    WalnutPi 2B / WalnutPi CM2
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_2/opencv/vision/plate_detection

import cv2

img = cv2.imread('car.png')   # Read the image

# Load the plate detection Haar cascade, the path must not contain non-ASCII characters
plateCascade = cv2.CascadeClassifier('data/haarcascade_russian_plate_number.xml')

# Detect every plate
plates = plateCascade.detectMultiScale(img, 1.15)

# Walk through every detected plate
for (x, y, w, h) in plates:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)   # Box the plate

cv2.imshow('result', img)   # Show the image

cv2.waitKey()                   # Wait for any key press
cv2.destroyAllWindows()         # Close the window
