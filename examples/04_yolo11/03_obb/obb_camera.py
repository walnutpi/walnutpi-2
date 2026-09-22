# What it does: Runs YOLO11 oriented bounding box detection on a live camera stream
# Wiring:       Connect a camera to the board
# Expected output: The live video is shown with rotated boxes, press space to quit
# Tested on:    WalnutPi 2B / WalnutPi CM2
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_2/npu/yolo/yolo11-obb

from walnutpi import YOLO11
import dataset_dota
import cv2

# [Optional] Allow Thonny to run remotely
import os
os.environ["DISPLAY"] = ":0.0"

path_model = "model/yolo11n-obb.nb"
yolo = YOLO11.YOLO11_OBB(path_model)

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

while True:

    # Read one frame from the camera
    ret, img = cap.read()

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Run inference on the image without blocking
    if not yolo.is_running:
        # Run detection with a confidence threshold of 0.6 and an IoU threshold of 0.1
        yolo.run_async(img, 0.6, 0.1)

    boxes = yolo.get_result()

    if boxes is not None:

        # Print the detection results
        print(f"boxes: {len(boxes)}")

        for box in boxes:
            print(
                "{:f} ({:4d},{:4d} r{:f} ) w{:4d} h{:4d} {:s}".format(
                    box.reliability,
                    box.x,
                    box.y,
                    box.angle,
                    box.w,
                    box.h,
                    dataset_dota.label_names[box.label],
                )
            )

        # Draw the boxes on the image
        for box in boxes:

            left_x = int(box.x - box.w / 2)
            left_y = int(box.y - box.h / 2)
            right_x = int(box.x + box.w / 2)
            right_y = int(box.y + box.h / 2)
            label = str(dataset_dota.label_names[box.label]) + " " + str(box.reliability)
            (label_width, label_height), bottom = cv2.getTextSize(
                label,
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                1,
            )

            cv2.line(img, box.get_top_left(), box.get_top_right(), (255, 255, 0), 2)
            cv2.line(img, box.get_top_left(), box.get_bottom_left(), (255, 255, 0), 2)
            cv2.line(img, box.get_bottom_right(), box.get_bottom_left(), (255, 255, 0), 2)
            cv2.line(img, box.get_bottom_right(), box.get_top_right(), (255, 255, 0), 2)
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

    cv2.imshow("result", img)   # Show the image in a window

    key = cv2.waitKey(1)   # Refresh the window every 1ms to avoid blocking
    if key == 32:          # Break when space is pressed
        break

cap.release()              # Release the camera
cv2.destroyAllWindows()    # Destroy the window
