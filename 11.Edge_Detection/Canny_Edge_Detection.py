import cv2
import numpy as np

# Canny Edge Detection:
# 1. Noise Reduction
# 2. Calculating the Intensity Gradient of the Image
# 3. Suppression of False Edges
# 4. Hysteresis Thresholding

image = cv2.imread("tiger.jpg")
cv2.imshow("Original Image", image)

img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image", img_gray)
img_blur = cv2.GaussianBlur(img_gray, (5, 5), 0)
cv2.imshow("Blurred Image", img_gray)

# Canny Edge Detection
edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200) 

cv2.imshow('Canny Edge Detection', edges)
cv2.imwrite("canny_edge.jpg", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
