# What it does: Runs YOLO11 pose estimation on a live camera stream and draws the skeleton
# Wiring:       Connect a camera to the board
# Expected output: The live video is shown with boxes, keypoints and skeleton, press space to quit
# Tested on:    WalnutPi 2B / WalnutPi CM2
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_2/npu/yolo/yolo11-pose

from walnutpi import YOLO11
import cv2

# [Optional] Allow Thonny to run remotely
import os
os.environ["DISPLAY"] = ":0.0"

label_names = ["person"]

model_path = "model/yolo11n-pose.nb"
yolo = YOLO11.YOLO11_POSE(model_path)

# Open the camera and loop over the frames to show them on screen
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

    # Read one frame and show it
    ret, img = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    if not yolo.is_running:
        yolo.run_async(img, 0.3)

    boxes = yolo.get_result()

    # Draw the boxes on the image
    for box in boxes:
        label = str(label_names[box.label]) + " " + str('%.2f' % box.reliability)
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

    cv2.imshow("result", img)   # Show the image in a window

    key = cv2.waitKey(1)   # Refresh the window every 1ms to avoid blocking
    if key == 32:          # Break when space is pressed
        break

cap.release()              # Release the camera
cv2.destroyAllWindows()    # Destroy the window
