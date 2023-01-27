import cv2

image = cv2.imread('one.jpg', 1)
cv2.line(image, (0, 0), (400, 400), (255, 0, 0), 5)
cv2.rectangle(image, (0, 0), (400, 400), (0, 255, 0), 4)
cv2.circle(image, (200, 200), 100, (0, 0, 255), -1)
cv2.putText(image, "Hello", (100, 100), cv2.FONT_HERSHEY_COMPLEX, 4, (10, 56, 167))
cv2.imshow("Photo Viewer", image)
cv2.waitKey(10000)
cv2.destroyAllWindows()