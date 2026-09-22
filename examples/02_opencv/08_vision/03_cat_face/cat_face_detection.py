# What it does: Detects cat faces in a photo with a Haar cascade classifier
# Wiring:       No wiring needed (reads cat.jpg and data/ from the current directory)
# Expected output: The photo is shown with every detected cat face boxed in red
# Tested on:    WalnutPi 2B / WalnutPi CM2
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_2/opencv/vision/cat_face_detection

import cv2

img = cv2.imread('cat.jpg')   # Read the image

# Load the cat face detection Haar cascade, the path must not contain non-ASCII characters
catFaceCascade = cv2.CascadeClassifier('data/haarcascade_frontalcatface.xml')

# Detect every cat face
catFaces = catFaceCascade.detectMultiScale(img, 1.15)

# Walk through every detected cat face
for (x, y, w, h) in catFaces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)   # Box the cat face

cv2.imshow('result', img)   # Show the image

cv2.waitKey()                   # Wait for any key press
cv2.destroyAllWindows()         # Close the window
