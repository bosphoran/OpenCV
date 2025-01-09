import cv2
 
# Reading the image
image = cv2.imread('sea.png')
 
# dividing height and width by 2 to get the center of the image
height = image.shape[0]
width = image.shape[1]
# get the center coordinates of the image to create the 2D rotation matrix
center = (width/2, height/2)
 
# using cv2.getRotationMatrix2D() to get the rotation matrix
rotate_matrix = cv2.getRotationMatrix2D(center, 180, 2) # cv2.getRotationMatrix2D(center, angle, scale)
 
# rotate the image using cv2.warpAffine
rotated_image = cv2.warpAffine(image, rotate_matrix, (width, height)) # cv2.warpAffine(src, M, dsize)
 
cv2.imshow('Original image', image)
cv2.imshow('Rotated image', rotated_image)
# wait indefinitely, press any key on keyboard to exit
cv2.waitKey(0)
# save the rotated image to disk
cv2.imwrite('rotated_image.jpg', rotated_image)

# Rotation is a three-step operation:
# First, you need to get the center of rotation. This typically is the center of the image you are trying to rotate.
# Next, create the 2D-rotation matrix. OpenCV provides the getRotationMatrix2D(). 
# Finally, apply the affine transformation to the image, using the rotation matrix. The warpAffine() function in OpenCV does the job.