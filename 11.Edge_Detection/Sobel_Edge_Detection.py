# How are Edges Detected?
# Sudden changes in pixel intensity characterize edges.
import cv2
import numpy as np

img = cv2.imread('tiger.jpg') 
cv2.imshow('Original', img)

# Convert to graycsale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Blur the image for better edge detection
# kernel = np.ones((5, 5), np.float32) / 25
img_blur = cv2.GaussianBlur(img_gray, (5, 5), 0) 
 
# Sobel Edge Detection
sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis
sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection
# Display Sobel Edge Detection Images
cv2.imshow('Sobel X', sobelx)
cv2.imshow('Sobel Y', sobely)
cv2.imshow('Sobel X Y using Sobel() function', sobelxy)
cv2.imwrite("sobel_edge.jpg", sobelxy)

cv2.waitKey(0)
cv2.destroyAllWindows()