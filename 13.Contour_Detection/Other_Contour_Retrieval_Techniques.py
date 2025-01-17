import cv2

# Contour Relationship Representation:
# The contour hierarchy is represented as an array, which in turn contains arrays of four values.
# It is represented as: [Next, Previous, First_Child, Parent] 

image2 = cv2.imread("img.jpg")
img_gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
ret, thresh2 = cv2.threshold(img_gray2, 150, 255, cv2.THRESH_BINARY)

# RETR_LIST:
# The RETR_LIST contour retrieval method does not create any parent child relationship between the extracted contours.
contours3, hierarchy3 = cv2.findContours(thresh2, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
image_copy4 = image2.copy()
cv2.drawContours(image_copy4, contours3, -1, (0, 255, 0), 2, cv2.LINE_AA)
# see the results
cv2.imshow('LIST', image_copy4)
print(f"LIST: {hierarchy3}")
# The 3rd and 4th index positions of all the detected contour areas are -1.
cv2.waitKey(0)

# RETR_EXTERNAL:
# It only detects the parent contours, and ignores any child contours.
contours4, hierarchy4 = cv2.findContours(thresh2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
image_copy5 = image2.copy()
cv2.drawContours(image_copy5, contours4, -1, (0, 255, 0), 2, cv2.LINE_AA)
# see the results
cv2.imshow('EXTERNAL', image_copy5)
print(f"EXTERNAL: {hierarchy4}")
# The output image shows only the points drawn on contours 1, 2, and 3. Contours 3a and 4 are omitted as they are child contours.
cv2.waitKey(0)

# RETR_CCOMP:
# Retrieves all the contours in an image. It also applies a 2-level hierarchy to all the shapes or objects in the image.
contours5, hierarchy5 = cv2.findContours(thresh2, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
image_copy6 = image2.copy()
cv2.drawContours(image_copy6, contours5, -1, (0, 255, 0), 2, cv2.LINE_AA)
cv2.imshow('CCOMP', image_copy6)
print(f"CCOMP: {hierarchy5}")
cv2.waitKey(0)

# RETR_TREE:
# Each contour can have its own hierarchy, in line with the level it is on, and the corresponding parent-child relationship that it has.
contours6, hierarchy6 = cv2.findContours(thresh2, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
image_copy7 = image2.copy()
cv2.drawContours(image_copy7, contours6, -1, (0, 255, 0), 2, cv2.LINE_AA)
# see the results
cv2.imshow('TREE', image_copy7)
print(f"TREE: {hierarchy6}")
cv2.waitKey(0)

cv2.destroyAllWindows()