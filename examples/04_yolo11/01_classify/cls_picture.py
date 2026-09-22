# What it does: Runs YOLO11 classification on a picture and shows the top 5 results
# Wiring:       No wiring needed (uses model/yolo11n-cls.nb and image/banana.jpg)
# Expected output: The top 5 labels are printed, drawn on the image and saved as result.jpg
# Tested on:    WalnutPi 2B / WalnutPi CM2
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_2/npu/yolo/yolo11-cls

from walnutpi import YOLO11
import dataset_ImageNet
import cv2

# [Optional] Allow Thonny to run remotely
import os
os.environ["DISPLAY"] = ":0.0"

model_path = "model/yolo11n-cls.nb"   # Model path
picture_path = "image/banana.jpg"     # Path of the image to classify
output_path = "result.jpg"            # Save the result to the current directory

img = cv2.imread(picture_path)   # Read the image

# Classify the image
yolo = YOLO11.YOLO11_CLS(model_path)
result = yolo.run(img)

# Print the results and draw them on the image
index = 0
for i in result.top5:

    show_string = "{:f} {:s}".format(
        i.reliability,
        dataset_ImageNet.label_names[i.label],
    )
    print(show_string)
    index += 1

    cv2.putText(
        img,
        show_string,
        (10, 30 * index),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 200),
        2,
    )

cv2.imwrite(output_path, img)   # Save the image

cv2.imshow('result', img)       # Show the image in a window

cv2.waitKey()                   # Wait for any key press
cv2.destroyAllWindows()         # Close the window
