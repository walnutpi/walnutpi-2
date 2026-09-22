# What it does: Runs YOLO11 pose estimation on a picture and draws the skeleton
# Wiring:       No wiring needed (uses model/yolo11n-pose.nb and image/person.jpg)
# Expected output: The box, keypoints and skeleton are drawn and saved as result.jpg
# Tested on:    WalnutPi 2B / WalnutPi CM2
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_2/npu/yolo/yolo11-pose

from walnutpi import YOLO11
import cv2

# [Optional] Allow Thonny to run remotely
import os
os.environ["DISPLAY"] = ":0.0"

label_names = ["person"]

model_path = "model/yolo11n-pose.nb"
picture_path = "image/person.jpg"
output_path = "result.jpg"

# Detect the image
yolo = YOLO11.YOLO11_POSE(model_path)
boxes = yolo.run(picture_path, 0.5, 0.5)

# Draw the boxes on the image
img = cv2.imread(picture_path)
for box in boxes:
    left_x = int(box.x - box.w / 2)
    left_y = int(box.y - box.h / 2)
    right_x = int(box.x + box.w / 2)
    right_y = int(box.y + box.h / 2)
    label = str(label_names[box.label]) + " " + str('%.2f' % (box.reliability))
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

    # 0 nose, 1 left eye, 2 right eye, 3 left ear, 4 right ear, 5 left shoulder, 6 right shoulder
    # 7 left elbow, 8 right elbow, 9 left wrist, 10 right wrist, 11 left hip, 12 right hip
    # 13 left knee, 14 right knee, 15 left ankle, 16 right ankle
    for i in box.keypoints:   # Draw every keypoint visible enough
        if i.visibility > 0.5:
            cv2.circle(img, i.xy, 5, (0, 0, 200), -1)

    # Connect the head
    cv2.line(img, box.keypoints[3].xy, box.keypoints[1].xy, (0, 255, 255), 2)
    cv2.line(img, box.keypoints[1].xy, box.keypoints[0].xy, (0, 255, 255), 2)
    cv2.line(img, box.keypoints[0].xy, box.keypoints[2].xy, (0, 255, 255), 2)
    cv2.line(img, box.keypoints[2].xy, box.keypoints[4].xy, (0, 255, 255), 2)
    cv2.line(img, box.keypoints[3].xy, box.keypoints[5].xy, (0, 255, 255), 2)
    cv2.line(img, box.keypoints[4].xy, box.keypoints[6].xy, (0, 255, 255), 2)

    # Connect the left and right arms
    cv2.line(img, box.keypoints[7].xy, box.keypoints[5].xy, (255, 0, 0), 2)
    cv2.line(img, box.keypoints[7].xy, box.keypoints[9].xy, (255, 0, 0), 2)
    cv2.line(img, box.keypoints[8].xy, box.keypoints[6].xy, (255, 0, 0), 2)
    cv2.line(img, box.keypoints[8].xy, box.keypoints[10].xy, (255, 0, 0), 2)

    # Connect the torso
    cv2.line(img, box.keypoints[5].xy, box.keypoints[6].xy, (100, 255, 100), 2)
    cv2.line(img, box.keypoints[11].xy, box.keypoints[5].xy, (100, 255, 100), 2)
    cv2.line(img, box.keypoints[12].xy, box.keypoints[6].xy, (100, 255, 100), 2)
    cv2.line(img, box.keypoints[12].xy, box.keypoints[11].xy, (100, 255, 100), 2)

    # Connect the left and right legs
    cv2.line(img, box.keypoints[13].xy, box.keypoints[11].xy, (255, 255, 0), 2)
    cv2.line(img, box.keypoints[13].xy, box.keypoints[15].xy, (255, 255, 0), 2)
    cv2.line(img, box.keypoints[14].xy, box.keypoints[12].xy, (255, 255, 0), 2)
    cv2.line(img, box.keypoints[14].xy, box.keypoints[16].xy, (255, 255, 0), 2)

cv2.imwrite(output_path, img)   # Save the image

cv2.imshow('result', img)       # Show the image in a window

cv2.waitKey()                   # Wait for any key press
cv2.destroyAllWindows()         # Close the window
