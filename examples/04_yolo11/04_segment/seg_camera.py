# What it does: Runs YOLO11 instance segmentation on a live camera stream
# Wiring:       Connect a camera to the board
# Expected output: The live video is shown with boxes and masks, press space to quit
# Tested on:    WalnutPi 2B / WalnutPi CM2
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_2/npu/yolo/yolo11-seg

from walnutpi import YOLO11
import dataset_coco
import cv2
import numpy as np

# [Optional] Allow Thonny to run remotely
import os
os.environ["DISPLAY"] = ":0.0"

model_path = "model/yolo11n-seg.nb"

# Detect the image
yolo = YOLO11.YOLO11_SEG(model_path)

# Open the camera and loop over the frames to show them on screen
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

# Switch to 1080p
#cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))
#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)    # Set the width
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)   # Set the height

while True:

    # Read one frame and show it
    ret, img = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    if not yolo.is_running:
        yolo.run_async(img, 0.5, 0.5)

    boxes = yolo.get_result()

    # Draw the boxes on the image
    for box in boxes:
        left_x = int(box.x - box.w / 2)
        left_y = int(box.y - box.h / 2)
        right_x = int(box.x + box.w / 2)
        right_y = int(box.y + box.h / 2)
        label = str(dataset_coco.label_names[box.label]) + " " + str('%.2f' % box.reliability)
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
        mask_img = np.zeros_like(img)               # Create a black image the same size as the source
        mask_img[box.mask > 200] = (0, 0, 255)      # Turn every mask pixel above 200 red
        img = cv2.addWeighted(img, 1, mask_img, 0.8, 0)   # Blend the mask with the source image

    cv2.imshow("result", img)   # Show the image in a window

    key = cv2.waitKey(1)   # Refresh the window every 1ms to avoid blocking
    if key == 32:          # Break when space is pressed
        break

cap.release()              # Release the camera
cv2.destroyAllWindows()    # Destroy the window
