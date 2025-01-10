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

# Define the blue color range in HSV
# HSV blue color: [206, 232, 168]
lower_blue = np.array([93, 160, 128])  # Lower bound of blue
upper_blue = np.array([113, 255, 208]) # Upper bound of blue

# Create a mask for green color
green_mask = cv2.inRange(hsv_image, lower_green, upper_green)
# Create a mask for blue color
blue_mask = cv2.inRange(hsv_image, lower_blue, upper_blue)
# Combine the masks using bitwise OR
combined_mask = cv2.bitwise_or(green_mask, blue_mask)

# Filter the green & blue colors from the original image using combined mask
result = cv2.bitwise_and(image, image, mask = combined_mask)
cv2.imwrite("green_blue.jpg", result)

# Display the results
cv2.imshow("Original Image", image)
cv2.imshow("Green & Blue Mask", combined_mask)
cv2.imshow("Filtered Green & Blue", result)

# Wait for a key press and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()
