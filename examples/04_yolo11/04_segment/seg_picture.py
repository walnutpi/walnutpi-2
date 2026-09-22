# What it does: Runs YOLO11 instance segmentation on a picture
# Wiring:       No wiring needed (uses model/yolo11n-seg.nb and image/000000371552.jpg)
# Expected output: The boxes and green masks are drawn on the image and saved as result.jpg
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
picture_path = "image/000000371552.jpg"
output_path = "result.jpg"

# Detect the image
yolo = YOLO11.YOLO11_SEG(model_path)
boxes = yolo.run(picture_path, 0.5, 0.5)

# Draw the boxes on the image
img = cv2.imread(picture_path)
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
    mask_img[box.mask > 200] = (0, 255, 0)      # Turn every mask pixel above 200 green
    img = cv2.addWeighted(img, 1, mask_img, 0.5, 0)   # Blend the mask with the source image

cv2.imwrite(output_path, img)   # Save the image

cv2.imshow('result', img)       # Show the image in a window

cv2.waitKey()                   # Wait for any key press
cv2.destroyAllWindows()         # Close the window
