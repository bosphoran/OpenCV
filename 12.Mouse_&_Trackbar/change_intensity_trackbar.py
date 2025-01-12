import cv2
import numpy as np

# Function to update the intensity of the image based on trackbar position
# alpha controls the contrast/intensity.
# beta is used to add brightness; here it’s set to 0 since we're only scaling the intensity.
def update_intensity(val):
    global original_image, image
    # Scale intensity: val ranges from 0 to 255
    intensity_scale = val / 255
    image = cv2.convertScaleAbs(original_image, alpha=intensity_scale, beta=0)
    cv2.imshow('Image', image)

# Load the original image
original_image = cv2.imread("mouse.jpg")
image = original_image.copy()

# Create a window
cv2.namedWindow('Image')

# Add a trackbar to adjust intensity
cv2.createTrackbar('Intensity', 'Image', 0, 255, update_intensity)

# Initialize with default intensity
cv2.setTrackbarPos('Intensity', 'Image', 127)  # Set default intensity to mid-level

# Show the image and wait for user input
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
