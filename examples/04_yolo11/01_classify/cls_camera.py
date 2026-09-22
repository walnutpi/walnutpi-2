# What it does: Runs YOLO11 classification on a live camera stream and shows the top 5 results
# Wiring:       Connect a camera to the board
# Expected output: The live video is shown with the top 5 labels and the FPS, press space to quit
# Tested on:    WalnutPi 2B / WalnutPi CM2
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_2/npu/yolo/yolo11-cls

from walnutpi import YOLO11
import dataset_ImageNet
import cv2
import time

# [Optional] Allow Thonny to run remotely
import os
os.environ["DISPLAY"] = ":0.0"

model_path = "model/yolo11n-cls.nb"
yolo = YOLO11.YOLO11_CLS(model_path)

# Open the camera
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

# Switch to 1080p
#cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))
#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)    # Set the width
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)   # Set the height

# Calculate the frame rate
count = 0
pt = 0
fps = 0

while True:

    # Calculate the frame rate
    count += 1
    if time.time() - pt >= 1:   # More than 1 second has passed

        fps = 1 / ((time.time() - pt) / count)   # Calculate the frame rate
        print(fps)
        count = 0
        pt = time.time()

    # Read one frame from the camera
    ret, img = cap.read()

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Run inference on the frame
    if not yolo.is_running:
        yolo.run_async(img)
    result = yolo.get_result()

    # Process the result
    index = 0

    if result is not None:

        for i in result.top5:

            show_string = "{:.2f} {:s}".format(i.reliability, dataset_ImageNet.label_names[i.label])

            index += 1

            print(show_string)   # Print the result

            # Draw the result
            cv2.putText(img, show_string, (10, 50 + 30 * index), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Draw the frame rate on the image
    cv2.putText(img, 'FPS: ' + str(fps), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow("result", img)   # Show the image in a window

    key = cv2.waitKey(1)   # Refresh the window every 1ms to avoid blocking
    if key == 32:          # Break when space is pressed
        break

cap.release()              # Release the camera
cv2.destroyAllWindows()    # Destroy the window
