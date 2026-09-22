# What it does: Detects license plates in a live USB camera stream with a Haar cascade classifier
# Wiring:       Connect a USB camera to a USB port
# Expected output: The live video is shown with every detected plate boxed in red and the FPS
# Tested on:    WalnutPi 2B / WalnutPi CM2
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_2/opencv/vision/plate_detection

import cv2
import time

# Load the plate detection Haar cascade, the path must not contain non-ASCII characters
plateCascade = cv2.CascadeClassifier('data/haarcascade_russian_plate_number.xml')

cam = cv2.VideoCapture(1)   # Open the USB camera

# A lower resolution speeds up detection, try 480x320 or 320x240
cam.set(3, 480)   # Set the capture width to 480
cam.set(4, 320)   # Set the capture height to 320

# Measure the frame rate
start = 0
end = 0

while True:

    start = time.time()         # Record the start time

    retval, img = cam.read()    # Read a frame from the camera

    # Detect every plate
    plates = plateCascade.detectMultiScale(img, 1.15)

    # Walk through every detected plate
    for (x, y, w, h) in plates:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)   # Box the plate

    end = time.time()   # Record the end time

    # Calculate the frame rate and round it to an integer
    fps = round(1 / (end - start))
    print('FPS: ', fps)

    # Draw the frame rate on the image
    cv2.putText(img, "FPS: " + str(fps), (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 5)

    cv2.imshow('result', img)   # Show the image

    key = cv2.waitKey(1)   # Refresh the window every 1ms to avoid blocking
    if key == 32:          # Break when space is pressed
        break

cam.release()              # Release the camera
cv2.destroyAllWindows()    # Destroy the window
