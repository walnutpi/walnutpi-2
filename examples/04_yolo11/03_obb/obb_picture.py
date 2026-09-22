# What it does: Runs YOLO11 oriented bounding box detection on a picture
# Wiring:       No wiring needed (uses model/yolo11n-obb.nb and image/plane.jpg)
# Expected output: The rotated boxes are printed, drawn on the image and saved as result.jpg
# Tested on:    WalnutPi 2B / WalnutPi CM2
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_2/npu/yolo/yolo11-obb

from walnutpi import YOLO11
import dataset_dota
import cv2

# [Optional] Allow Thonny to run remotely
import os
os.environ["DISPLAY"] = ":0.0"

model_path = "model/yolo11n-obb.nb"
picture_path = "image/plane.jpg"
output_path = "result.jpg"

# Detect the image
yolo = YOLO11.YOLO11_OBB(model_path)
boxes = yolo.run(picture_path, 0.6, 0.1)

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
img = cv2.imread(picture_path)
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

cv2.imwrite(output_path, img)   # Save the image

cv2.imshow('result', img)       # Show the image in a window

cv2.waitKey()                   # Wait for any key press
cv2.destroyAllWindows()         # Close the window
