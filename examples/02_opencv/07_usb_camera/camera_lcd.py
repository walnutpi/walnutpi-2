# What it does: Shows a USB camera stream fullscreen on the LCD
# Wiring:       Connect a USB camera to a USB port
# Expected output: The live video fills the screen, press space to quit
# Tested on:    WalnutPi 2B / WalnutPi CM2
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_2/opencv/lcd

import cv2

# Create a borderless fullscreen window
cv2.namedWindow('Video', cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty('Video', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

cam = cv2.VideoCapture(1)   # Open the camera

while cam.isOpened():   # Make sure the camera is open

    retval, img = cam.read()   # Read a frame from the camera

    cv2.imshow("Video", img)   # Show the frame in the window

    key = cv2.waitKey(1)   # Refresh the window every 1ms to avoid blocking

    if key == 32:   # Break when space is pressed
        break

cam.release()              # Release the camera
cv2.destroyAllWindows()    # Destroy the window
