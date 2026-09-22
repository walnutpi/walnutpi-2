# What it does: Finds the single best template match in an image
# Wiring:       No wiring needed (reads number.jpg and 2.jpg from the current directory)
# Expected output: The match result is printed and the match is boxed in red
# Tested on:    WalnutPi 2B / WalnutPi CM2
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_2/opencv/detection/template_match

import cv2

img = cv2.imread('number.jpg')   # Read the source image
temp = cv2.imread('2.jpg')       # Read the template image

h, w, c = temp.shape   # Get the template size, height, width and channel count

# Match with the normalized square difference method, a smaller result means a better match
result = cv2.matchTemplate(img, temp, cv2.TM_SQDIFF_NORMED)

print(result)   # Print the result

# Single target match, minValue is the match result and minLoc is its top left corner
minValue, maxValue, minLoc, maxLoc = cv2.minMaxLoc(result)

# Draw a rectangle to show the match
p1 = minLoc                        # Top left corner of the rectangle
p2 = (p1[0] + w, p1[1] + h)        # Bottom right corner of the rectangle
cv2.rectangle(img, p1, p2, (0, 0, 255), 2)

cv2.imshow('result', img)      # Show the image

cv2.waitKey()                   # Wait for any key press
cv2.destroyAllWindows()         # Close the window
