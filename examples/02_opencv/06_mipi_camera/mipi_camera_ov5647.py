# What it does: Captures a live stream from a MIPI OV5647 camera
# Wiring:       Connect the OV5647 camera to the MIPI CSI connector, it must be enumerated as video0
# Expected output: The live video is shown in a window, press space to quit
# Tested on:    WalnutPi 2B / WalnutPi CM2
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_2/os_software/mipi_cam

import cv2
from walnutpi import isp

cam = cv2.VideoCapture(0)   # Open the camera, make sure the index is correct, video0

# Declare that the camera transfers frames in NV12 format
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('N', 'V', '1', '2'))

isp.start(camera=0)   # Must match the camera index above, video0

# Set the resolution, the default is 640x480
#cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
#cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

while cam.isOpened():   # Make sure the camera is open

    retval, img = cam.read()   # Read a frame from the camera

    cv2.imshow("Video", img)   # Show the frame in the window

    key = cv2.waitKey(1)   # Refresh the window every 1ms to avoid blocking

    if key == 32:   # Break when space is pressed
        break

cam.release()              # Release the camera
cv2.destroyAllWindows()    # Destroy the window
