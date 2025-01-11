import cv2
import numpy as np

# Global thresholding is when the thresholding rule is applied equally to every pixel in the image, and the threshold value is fixed.

src = cv2.imread("threshold.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Original Image", src)
 
# Set threshold and maxValue
thresh = 40
maxValue = 225
# Binary Thresholding:
# At each pixel location (x,y), the pixel intensity at that location is compared to  a threshold value, thresh.
# If src(x,y) is greater than thresh, the thresholding operation sets the value of the destination image pixel dst(x,y) to the maxValue. 
# Otherwise, it sets it to 0

# Simple threshold function pseudo code
# if src(x,y) > thresh
#   dst(x,y) = maxValue
# else
#   dst(x,y) = 0

# Basic threhold example
th, dst = cv2.threshold(src, thresh, maxValue, cv2.THRESH_BINARY);
cv2.imwrite("opencv-threshold-example.jpg", dst)
cv2.imshow("Binary Thresholding", dst)
 
# Thresholding using THRESH_BINARY_INV
# The destination pixel is set to zero, if the corresponding source pixel is greater than the threshold. 
# It is set to maxValue, if the source pixel is less than the threshold.
th, dst = cv2.threshold(src, thresh, maxValue, cv2.THRESH_BINARY_INV)
cv2.imwrite("opencv-thresh-binary-inv.jpg", dst)
cv2.imshow("Binary Inverse Thresholding", dst)
 
# Thresholding using THRESH_TRUNC
# The destination pixel is set to the threshold (thresh), if the source pixel value is greater than the threshold.
# Otherwise, it is set to the source pixel value. The maxValue is ignored
th, dst = cv2.threshold(src, thresh, maxValue, cv2.THRESH_TRUNC)
cv2.imwrite("opencv-thresh-trunc.jpg", dst)
cv2.imshow("Truncate Thresholding", dst)
 
# Thresholding using THRESH_TOZERO 
# The destination pixel value is set to the pixel value of the corresponding source , 
# if the source pixel value is greater than the threshold. Otherwise, it is set to zero. The maxValue is ignored
th, dst = cv2.threshold(src, thresh, maxValue, cv2.THRESH_TOZERO)
cv2.imwrite("opencv-thresh-tozero.jpg", dst)
cv2.imshow("Threshold to Zero", dst)
 
# Thresholding using THRESH_TOZERO_INV 
# The destination pixel value is set to zero, if the source pixel value is greater than the threshold. 
# Otherwise, it is set to the source pixel value. The  maxValue is ignored.
th, dst = cv2.threshold(src, thresh, maxValue, cv2.THRESH_TOZERO_INV)
cv2.imwrite("opencv-thresh-to-zero-inv.jpg", dst)
cv2.imshow("Inverted Threshold to Zero", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()