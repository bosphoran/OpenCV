# Using contour detection, we can detect the borders of objects
# What are Contours:
# When we join all the points on the boundary of an object, we get a contour. 
# Typically, a specific contour refers to boundary pixels that have the same color and intensity.

import cv2

image = cv2.imread("contour.jpg")
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", image_gray)

# apply binary thresholding
ret, thresh = cv2.threshold(image_gray, 110, 255, cv2.THRESH_BINARY)
cv2.imshow('Binary image', thresh)

# detect the contours on the binary image using cv2.CHAIN_APPROX_NONE
contours, hierarchy = cv2.findContours(image = thresh, method = cv2.CHAIN_APPROX_NONE, mode = cv2.RETR_TREE)
                                      
# draw contours on the original image
image_copy = image.copy()
cv2.drawContours(image=image_copy, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)

cv2.imshow('None Approximation Method', image_copy)
cv2.imwrite('contours_none_approx.jpg', image_copy)


cv2.waitKey(0)
cv2.destroyAllWindows()