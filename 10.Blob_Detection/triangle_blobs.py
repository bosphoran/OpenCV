import cv2
import numpy as np

# Load the image
image = cv2.imread("blob.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply GaussianBlur to reduce noise
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Detect edges using Canny edge detection
edges = cv2.Canny(blurred, 50, 150)

# Find contours in the edged image
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Loop over contours to detect triangles
for contour in contours:
    # Approximate the contour to reduce the number of points
    epsilon = 0.04 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)

    # If the approximated contour has 3 vertices, it's a triangle
    if len(approx) == 3:
        cv2.drawContours(image, [approx], 0, (85, 42, 255), 2)

# Display the resulting image with detected triangles
cv2.imshow("Triangles Detected", image)
cv2.imwrite("Triangle_blob.jpg", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
