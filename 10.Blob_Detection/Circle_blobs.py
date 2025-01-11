import cv2
import numpy as np

# A Blob is a group of connected pixels in an image that share some common property ( E.g, grayscale value ). 
# # Set up the detector with default parameters.
# detector = cv2.SimpleBlobDetector()
# # Detect blobs.
# keypoints = detector.detect(image)
# # Draw detected blobs as red circles.

image = cv2.imread("blob.jpg", cv2.IMREAD_GRAYSCALE)

# Set up the SimpleBlobDetector parameters
params = cv2.SimpleBlobDetector_Params()

# Filter by circularity (adjust to focus on circular blobs)
params.filterByCircularity = True
params.minCircularity = 0.9  # Minimum circularity
params.maxCircularity = 1.0  # Maximum circularity

# Filter by area to exclude small or excessively large shapes
params.filterByArea = True
params.minArea = 100  # Minimum area
params.maxArea = 5000  # Maximum area

# Disable other filters to focus on circles
params.filterByConvexity = False
params.filterByInertia = False
params.filterByColor = False

# Create a blob detector with the parameters
detector = cv2.SimpleBlobDetector_create(params)

# Detect blobs
keypoints = detector.detect(image)

# Draw detected blobs as red circles
im_with_keypoints = cv2.drawKeypoints(
    image, keypoints, np.array([]), (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Display the resulting image with detected circles
cv2.imshow("Detected Circles", im_with_keypoints)
cv2.imwrite("circle_blobs.jpg", im_with_keypoints)
cv2.waitKey(0)
cv2.destroyAllWindows()

