import cv2
import numpy as np

# Load the image
image = cv2.imread("bright.png")

# Convert the image to HSV color space
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Hue: 0–179, ± 10
# Saturation: 0–255, ± 40
# Value: 0–255, ± 40

# Define the green color range in HSV
lower_green = np.array([35, 100, 100])  # Lower bound of green
upper_green = np.array([85, 255, 255]) # Upper bound of green

# Create a mask for green color
green_mask = cv2.inRange(hsv_image, lower_green, upper_green)

# Filter the green color from the original image
green_result = cv2.bitwise_and(image, image, mask = green_mask)
cv2.imwrite("green_space.jpg", green_result)

# Display the results
cv2.imshow("Original Image", image)
cv2.imshow("Green Mask", green_mask)
cv2.imshow("Filtered Green", green_result)

# Wait for a key press and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()
