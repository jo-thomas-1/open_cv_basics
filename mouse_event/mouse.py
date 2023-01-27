import cv2

def draw_circle(event, x, y, flag, params):
	if event == cv2.EVENT_LBUTTONUP:
		print("Event: ", event)
		print("x, y: ", x, y)
		cv2.circle(image, (x, y), 100, (255, 0, 0), -1)

image = cv2.imread('one.jpg', 1)

cv2.namedWindow("image")
cv2.setMouseCallback("image", draw_circle)
cv2.imshow("image", image)

while True:
	cv2.imshow("image", image)
	if cv2.waitKey(20) & 0xff == ord('q'):
		break

cv2.destroyAllWindows()