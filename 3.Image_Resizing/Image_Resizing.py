# let's start with the Imports 
import cv2
import numpy as np
 
# Read the image using imread function
image = cv2.imread('car.jpg')
cv2.imshow('Original Image', image)

# Get original height and width
height, width, c = image.shape
print("Original Height and Width:", height, "x", width)

scale_up = 50
scale_down = 150

# let's downscale the image using new  width and height
down_height = int(height * scale_down / 100)
down_width= int(width * scale_down / 100)
down_points = (down_width, down_height)
interpolation = cv2.INTER_AREA # Best for downscaling images.
resized_down = cv2.resize(image, down_points, interpolation)
 
# let's upscale the image using new  width and height
up_height = int(height * scale_up / 100)
up_width = int(width * scale_up / 100)
up_points = (up_width, up_height)
interpolation = cv2.INTER_LINEAR # General-purpose interpolation for upscaling and downscaling.
resized_up = cv2.resize(image, up_points, interpolation)
 
# Display images
cv2.imshow('Resized Down by defining height and width', resized_down)
cv2.waitKey()
cv2.imshow('Resized Up image by defining height and width', resized_up)
cv2.waitKey()
 
#press any key to close the windows
cv2.destroyAllWindows()