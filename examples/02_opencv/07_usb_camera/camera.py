# What it does: Captures a live stream from a USB camera
# Wiring:       Connect a USB camera to a USB port
# Expected output: The live video is shown in a window, press space to quit
# Tested on:    WalnutPi 2B / WalnutPi CM2
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_2/opencv/usb_cam

import cv2

cam = cv2.VideoCapture(1)   # Open the camera

while cam.isOpened():   # Make sure the camera is open

    retval, img = cam.read()   # Read a frame from the camera

    cv2.imshow("Video", img)   # Show the frame in the window

    key = cv2.waitKey(1)   # Refresh the window every 1ms to avoid blocking

    if key == 32:   # Break when space is pressed
        break

cam.release()              # Release the camera
cv2.destroyAllWindows()    # Destroy the window
