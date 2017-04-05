import argparse
import cv2
 
"""
In order to find bigShoeBox bounding box position, made this script.

control:
mouse click on picture screen to get x,y value of click position.

press c to break
"""
index = 0
 
def click_and_crop(event, x, y, flags, param):
	# grab references to the global variables
	global index
	# if the left mouse button was clicked, record the starting
	# (x, y) coordinates and indicate that cropping is being
	# performed
	if event == cv2.EVENT_LBUTTONDOWN:
		print(index, [x, y])
		index = index + 1

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())
 
# load the image, clone it, and setup the mouse callback function
image = cv2.imread(args["image"])
clone = image.copy()
cv2.namedWindow("image")
cv2.setMouseCallback("image", click_and_crop)
 
# keep looping until the 'q' key is pressed
while True:
	# display the image and wait for a keypress
	cv2.imshow("image", image)
	key = cv2.waitKey(1) & 0xFF
 
	# if the 'c' key is pressed, break from the loop
	if key == ord("c"):
		break
 
# close all open windows
cv2.destroyAllWindows()