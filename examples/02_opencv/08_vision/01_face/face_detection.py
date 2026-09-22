# What it does: Detects faces in a photo with a Haar cascade classifier
# Wiring:       No wiring needed (reads face1.jpg and data/ from the current directory)
# Expected output: The photo is shown with every detected face boxed in red
# Tested on:    WalnutPi 2B / WalnutPi CM2
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_2/opencv/vision/front_face_detection

import cv2

img = cv2.imread('face1.jpg')   # Read the image

# Load the face detection Haar cascade, the path must not contain non-ASCII characters
faceCascade = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

# Detect every face
faces = faceCascade.detectMultiScale(img, 1.2)

# Walk through every detected face
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)   # Box the face

cv2.imshow('result', img)   # Show the image

cv2.waitKey()                   # Wait for any key press
cv2.destroyAllWindows()         # Close the window
