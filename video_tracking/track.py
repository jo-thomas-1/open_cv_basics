import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
	_, frame = cap.read()

	# convert color space to HSV
	new_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	lower_blue = np.array([110, 50, 50])
	upper_blue = np.array([130, 252, 255])
	mask = cv2.inRange(new_image, lower_blue, upper_blue)

	result = cv2.bitwise_and(frame, frame, mask=mask)
	cv2.imshow("Result", result)

	if cv2.waitKey(20) & 0xff == ord('q'):
		break

cv2.destroyAllWindows()