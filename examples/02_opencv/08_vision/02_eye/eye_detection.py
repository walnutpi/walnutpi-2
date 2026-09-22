# What it does: Detects eyes in a photo with a Haar cascade classifier
# Wiring:       No wiring needed (reads eye.jpg and data/ from the current directory)
# Expected output: The photo is shown with every detected eye boxed in red
# Tested on:    WalnutPi 2B / WalnutPi CM2
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_2/opencv/vision/eye_detection

import cv2

img = cv2.imread('eye.jpg')   # Read the image

# Load the eye detection Haar cascade, the path must not contain non-ASCII characters
eyeCascade = cv2.CascadeClassifier('data/haarcascade_eye.xml')

# Detect every eye
eyes = eyeCascade.detectMultiScale(img, 1.2)

# Walk through every detected eye
for (x, y, w, h) in eyes:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)   # Box the eye

cv2.imshow('result', img)   # Show the image

cv2.waitKey()                   # Wait for any key press
cv2.destroyAllWindows()         # Close the window
