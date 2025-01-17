import cv2

image = cv2.imread("simple.jpg")
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", image_gray)

# apply binary thresholding
ret, thresh = cv2.threshold(image_gray, 150, 255, cv2.THRESH_BINARY)
cv2.imshow('Binary image', thresh)

# detect the contours on the binary image using cv2.ChAIN_APPROX_SIMPLE
contours1, hierarchy1 = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# draw contours on the original image for `CHAIN_APPROX_SIMPLE`
image_copy1 = image.copy()
cv2.drawContours(image_copy1, contours1, -1, (0, 255, 0), 2, cv2.LINE_AA)
# see the results
cv2.imshow('Simple approximation', image_copy1)
cv2.waitKey(0)

image_copy2 = image.copy()
for i, contour in enumerate(contours1): # loop over one contour area
   for j, contour_point in enumerate(contour): # loop over the points
       # draw a circle on the current contour coordinate
       cv2.circle(image_copy2, ((contour_point[0][0], contour_point[0][1])), 2, (0, 255, 0), 2, cv2.LINE_AA)
# see the results
cv2.imshow('CHAIN_APPROX_SIMPLE Point only', image_copy2)
cv2.imwrite('contour_point_simple.jpg', image_copy2)

cv2.waitKey(0)
cv2.destroyAllWindows()