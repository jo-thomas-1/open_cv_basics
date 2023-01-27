import cv2

image = cv2.imread('one.jpg', 1)
print(image)
cv2.imshow("Photo Viewer", image)
cv2.waitKey(10000)
cv2.destroyAllWindows()