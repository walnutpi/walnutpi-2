# What it does: Runs YOLO11 object detection on a picture and boxes every detected object
# Wiring:       No wiring needed (uses model/yolo11n.nb and image/bus.jpg)
# Expected output: The boxes are printed, drawn on the image and saved as result.jpg
# Tested on:    WalnutPi 2B / WalnutPi CM2
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_2/npu/yolo/yolo11-detect

from walnutpi import YOLO11
import dataset_coco
import cv2

# [Optional] Allow Thonny to run remotely
import os
os.environ["DISPLAY"] = ":0.0"

path_model = "model/yolo11n.nb"   # Model path
path_image = "image/bus.jpg"      # Path of the image to detect
output_path = "result.jpg"        # Save the result to the current directory

img = cv2.imread(path_image)   # Read the image

# Detect the image
yolo = YOLO11.YOLO11_DET(path_model)

# Run object detection with a confidence threshold of 0.5 and an IoU threshold of 0.45
boxes = yolo.run(img, 0.5, 0.45)

# Print the detection results
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
    left_x = int(box.x - box.w / 2)
    left_y = int(box.y - box.h / 2)
    right_x = int(box.x + box.w / 2)
    right_y = int(box.y + box.h / 2)
    label = str(dataset_coco.label_names[box.label]) + " " + str(box.reliability)
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

cv2.imwrite(output_path, img)   # Save the image

cv2.imshow('result', img)       # Show the image in a window

cv2.waitKey()                   # Wait for any key press
cv2.destroyAllWindows()         # Close the window
