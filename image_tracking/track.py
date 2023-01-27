import cv2
import numpy as np

image = cv2.imread('one.jpg')
cv2.imshow("Original", image)

# convert color space to HSV
new_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

cv2.imshow("HSV Image", new_image)

lower_blue = np.array([110, 50, 50])
upper_blue = np.array([130, 252, 255])
mask = cv2.inRange(new_image, lower_blue, upper_blue)
cv2.imshow("Mask", mask)

result = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Result", result)

cv2.waitKey(0)
cv2.destroyAllWindows()