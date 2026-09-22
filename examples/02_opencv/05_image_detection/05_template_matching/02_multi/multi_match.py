# What it does: Finds every template match above a threshold in an image
# Wiring:       No wiring needed (reads number.jpg and 2.jpg from the current directory)
# Expected output: The number of matches is printed and every match is boxed in red
# Tested on:    WalnutPi 2B / WalnutPi CM2
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_2/opencv/detection/template_match

import cv2

img = cv2.imread('number.jpg')   # Read the source image
temp = cv2.imread('2.jpg')       # Read the template image

h, w, c = temp.shape   # Get the template size, height, width and channel count

# Match with the normalized correlation method, a larger result means a better match
result = cv2.matchTemplate(img, temp, cv2.TM_CCORR_NORMED)

print(result)   # Print the result

# Evaluate the match result and draw the rectangles
num = 0   # Count the number of matches

for y in range(len(result)):          # Walk through every row
    for x in range(len(result[y])):   # Walk through every column

        # Raise the threshold for a stricter match and fewer results, it must stay below 1
        if result[y][x] > 0.999:

            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)   # Draw the rectangle

            num = num + 1

# Print the match count, try 0.9 or 0.999 to see how the count changes
print(num)

cv2.imshow('result', img)      # Show the image

cv2.waitKey()                   # Wait for any key press
cv2.destroyAllWindows()         # Close the window
