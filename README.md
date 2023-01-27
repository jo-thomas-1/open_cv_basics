# OpenCV

OpenCV is a library of programming functions mainly aimed at real-time computer vision. Originally developed by Intel in 1999, it was later supported by Willow Garage then Itseez. The library is cross-platform and free for use under the open-source Apache 2 License.

Website: https://opencv.org/
Documentation: https://docs.opencv.org/4.x/

OpenCV-Python is the Python API form OpenCV.

- install the library using the command `pip install opencv-python`
- when writting code `import cv2`

## Images

- the below code uses OpenCV to read and display an image
- first import OpenCV as `import cv2`
- create the image instance with `imread`
- imread takes the name or relative path to image file and the flag used to specify a color sceme
	- 1 or `cv2.IMREAD_COLOR` to load a color image. Any transparency of image will be neglected. It is the default flag
	- 0 or `cv2.IMREAD_GRAYSCALE` to load an image in grayscale mode
	- -1 `cv2.IMREAD_UNCHANGED` to load an image as it is including alpha channel

```
import cv2

image = cv2.imread('alita.jpg', 1)
cv2.imshow("image", image)
cv2.waitKey(10000)
cv2.destroyAllWindows()
```

- passing the image instance to print statement will print out the pixel value matrix of the image

## Webcam

- the below code uses OpenCV to read and display the video footage from the selected video source
- when creating the instance of `VideoCapture`, it accepts one argument to select the source device. 0 is given for default device.

```
import cv2

capture = cv2.VideoCapture(0)

while True:
	ret, frame = capture.read(0)
	cv2.imshow('image', frame)
	if cv2.waitKey(1) and 0xff == ord('q'):
		break

capture.release()
cv2.destroyAllWindows()
```

- the below code can be inserted instead of `cv2.imshow('image', frame)` to view the video in greyscale

```
grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
cv2.imshow('image', grey)
```

- `cv2.waitkey(1)` waits for 1 ms and returns the code of the key on keyboard if it is pressed
- `0xff` is the hexadecimal notation for 255
- `ord()` function returns the Unicode code of the character passed in arguments
- the below section of code is used to check if the letter 'q' has been pressed on the keyboard

## Draw on Images

OpenCV provides option to draw shapes on images and return them as an image.

```
import cv2

image = cv2.imread('one.jpg', 1)
cv2.line(image, (0, 0), (400, 400), (255, 0), 5)
cv2.imshow("Photo Viewer", image)
cv2.waitKey(10000)
cv2.destroyAllWindows()
```

- Line - cv2.line(image, start_point, end_point, color, thickness)
	- image - the image on which line is to be drawn
	- start_point - starting coordinates of the line. represented as tuples of X coordinate value and Y coordinate value
	- end_point: ending coordinates of the line. represented as tuples of X coordinate value and Y coordinate value
	- color - color of the line to be drawn. represented as RGB as a tuple
	- thickness - thickness of the line in px
	- eg: `cv2.line(image, (0, 0), (400, 400), (255, 0, 0), 5)`

- Rectangle - cv2.rectangle(image, start_point, end_point, color, thickness)
	- image - the image on which rectangle is to be drawn
	- start_point - starting coordinates of rectangle. represented as tuples of X coordinate value and Y coordinate value
	- end_point - ending coordinates of rectangle. represented as tuples of X coordinate value and Y coordinate value
	- color - color of border line of rectangle to be drawn. represented as RGB as a tuple
	- thickness - thickness of the rectangle border line in px. thickness of -1 px will fill the rectangle shape by the specified color
	- eg: `cv2.rectangle(image, (0, 0), (400, 400), (255, 0, 0), 5)`

- Circle - cv2.circle(image, center_coordinates, radius, color, thickness)
	- image - the image on which the circle is to be drawn
	- center_coordinates - the center coordinates of the circle. coordinates are represented as tuples of X coordinate value and Y coordinate value
	- radius - radius of the circle
	- color - the color of the borderline of a circle to be drawn. represented as RGB as a tuple
	- thickness - the thickness of the circle border line in px. thickness of -1 px will fill the circle shape by the specified color
	- eg: `cv2.circle(image, (400, 400), 5, (255, 0, 0), 4)`

- Text - cv2.putText(image, text, org, font, fontScale, color [, thickness [, lineType [, bottomLeftOrigin ]]])
	- image - the image on which the circle is to be drawn
	- text - text string to be drawn
	- org - the coordinates of the bottom-left corner of the text string in the image. coordinates are represented as tuples of X coordinate value and Y coordinate value
	- font - it denotes the font type. some font types are FONT_HERSHEY_SIMPLEX, FONT_HERSHEY_PLAIN, etc.
	- fontScale - font scale factor that is multiplied by the font-specific base size
	- color - the color of text string to be drawn. represented as RGB as a tuple
	- thickness - the thickness of the line in px
	- lineType - (optional parameter) the type of the line to be used
	- bottomLeftOrigin - (optional parameter) when given as true, the image data origin is at the bottom-left corner. otherwise, it is at the top-left corner
	- eg: `cv2.putText(image, "Hello", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 3)`

```
import cv2

image = cv2.imread('one.jpg', 1)
cv2.line(image, (0, 0), (400, 400), (255, 0, 0), 5)
cv2.rectangle(image, (0, 0), (400, 400), (0, 255, 0), 4)
cv2.circle(image, (200, 200), 100, (0, 0, 255), -1)
cv2.putText(image, "Hello", (100, 100), cv2.FONT_HERSHEY_COMPLEX, 4, (10, 56, 167))
cv2.imshow("Photo Viewer", image)
cv2.waitKey(10000)
cv2.destroyAllWindows()
```

## Mouse Event

- performs actions based on mouse events
- the below code creates a circle on the image with the position of mouse click as its center
- there are many other constants that can be used like `EVENT_LBUTTONUP`, each representing a mouse action

```
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
```

## Color Space

Color spaces are a way to represent the color channels present in the image that gives the image that particular hue. There are several different color spaces and each has its own significance. Some of the popular color spaces are RGB (Red, Green, Blue), CMYK (Cyan, Magenta, Yellow, Black), HSV (Hue, Saturation, Value), etc.

OpenCV's default color space is RGB. However, it actually stores color in the BGR format. It is an additive color model where the different intensities of Blue, Green and Red give different shades of color.

- it is a way to define color for each pixel in an image
- BGR (Blue, Green, Red) is the color space used in most of the above sections
- they can be converted into any other color space as required
- there are more than 150 color space convertion methods available
- the `cv2.cvtColor()` method can be used to convert color space
- the below code shows how OpenCV can split these colors

```
import cv2

image = cv2.imread('one.jpg')
B, G, R = cv2.split(image)

# Corresponding channels are separated

cv2.imshow("original", image)
cv2.waitKey(0)
cv2.destroyWindow("original")

cv2.imshow("blue", B)
cv2.waitKey(0)
cv2.destroyWindow("blue")

cv2.imshow("Green", G)
cv2.waitKey(0)
cv2.destroyWindow("Green")

cv2.imshow("red", R)
cv2.waitKey(0)

cv2.destroyAllWindows()
```

### HSV

HSV (Hue, Saturation, Value) color space is considerably closer to RGB color space in which humans describe color sensations and perceive colors.

- Hue is the dominant color. ranges from 0 to 360
- Saturation is the amount of gray. ranges from 0% to 100%
- Value is the brightness / intensity of the color. ranges from 0 to 100

eg: `cv2.cvtColor(image, cv2.COLOR_BGR2HSV)`

## Image Tracking

- image tracking is done by analysing the pixels
- the system looks for the specific colors mentioned and marks them
- the below code tracks blue colored objects from the provided image

```
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
```

## Video Tracking

- the same as image tracking but here the object is a video
- so each frame is captured as an image and the same functionality as in the previous section is repeated

```
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
```

## Example Projects

The following are some sample projects created based on the above documentation.

| # | Name | Action |
|---|---|---|
| 1 | Images | [Go to code](https://github.com/jothomas1996/open_cv_basics/tree/main/image) |
| 2 | Webcam | [Go to code](https://github.com/jothomas1996/open_cv_basics/tree/main/webcam) |
| 3 | Draw on image | [Go to code](https://github.com/jothomas1996/open_cv_basics/tree/main/draw_on_images) |
| 4 | Mouse Event | [Go to code](https://github.com/jothomas1996/open_cv_basics/tree/main/mouse_event) |
| 5 | Color Space | [Go to code](https://github.com/jothomas1996/open_cv_basics/tree/main/color_space) |
| 6 | Image Tracking | [Go to code](https://github.com/jothomas1996/open_cv_basics/tree/main/image_tracking) |
| 7 | Video Tracking | [Go to code](https://github.com/jothomas1996/open_cv_basics/tree/main/video_tracking) |