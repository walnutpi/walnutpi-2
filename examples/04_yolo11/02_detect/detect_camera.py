# What it does: Runs YOLO11 object detection on a live camera stream and boxes every object
# Wiring:       Connect a camera to the board
# Expected output: The live video is shown with the boxes and the FPS, press space to quit
# Tested on:    WalnutPi 2B / WalnutPi CM2
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_2/npu/yolo/yolo11-detect

from walnutpi import YOLO11
import dataset_coco
import cv2
import time

# [Optional] Allow Thonny to run remotely
import os
os.environ["DISPLAY"] = ":0.0"

path_model = "model/yolo11n.nb"
yolo = YOLO11.YOLO11_DET(path_model)

# Open the camera
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

# Switch to 1080p
#cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))
#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)    # Set the width
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)   # Set the height

boxes = []

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

    # Run inference on the image without blocking
    if not yolo.is_running:
        # Run object detection with a confidence threshold of 0.5 and an IoU threshold of 0.45
        yolo.run_async(img, 0.5, 0.45)

    boxes = yolo.get_result()

    # Print the detection results
    if boxes is not None:
        print(f"boxes: {len(boxes)}")
        for box in boxes:
            print(
                "{:f} ({:4d},{:4d}) w{:4d} h{:4d} {:s}".format(
                    box.reliability,
                    box.x,
                    box.y,
                    box.w,
                    box.h,
                    dataset_coco.label_names[box.label],
                )
            )

    # Draw the boxes on the image
    for box in boxes:
        label = str(dataset_coco.label_names[box.label]) + " " + str('%.2f' % box.reliability)
        left_x = int(box.x - box.w / 2)
        left_y = int(box.y - box.h / 2)
        right_x = int(box.x + box.w / 2)
        right_y = int(box.y + box.h / 2)
        (label_width, label_height), bottom = cv2.getTextSize(
            label,
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            1,
        )
        cv2.rectangle(
            img,
            (left_x, left_y),
            (right_x, right_y),
            (255, 255, 0),
            2,
        )
        cv2.rectangle(
            img,
            (left_x, left_y - label_height * 2),
            (left_x + label_width, left_y),
            (255, 255, 255),
            -1,
        )
        cv2.putText(
            img,
            label,
            (left_x, left_y - label_height),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 0, 0),
            1,
        )

    # Draw the frame rate on the image
    cv2.putText(img, 'FPS: ' + str(fps), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow("result", img)   # Show the image in a window

    key = cv2.waitKey(1)   # Refresh the window every 1ms to avoid blocking
    if key == 32:          # Break when space is pressed
        break

cap.release()              # Release the camera
cv2.destroyAllWindows()    # Destroy the window
