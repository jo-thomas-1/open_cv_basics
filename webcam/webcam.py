import cv2

capture = cv2.VideoCapture(0)

while True:
	ret, frame = capture.read(0)
	# grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	# cv2.imshow('image', grey)
	cv2.imshow('Webcam', frame)
	if cv2.waitKey(1) & 0xff == ord('q'):
		break

capture.release()
cv2.destroyAllWindows()