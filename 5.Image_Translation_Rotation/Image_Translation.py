import cv2
import numpy as np

image = cv2.imread("sea.png")

height = image.shape[0]
width = image.shape[1]

# get tx and ty values for translation
# you can specify any value of your choice
tx, ty = int(width/4), int(height/4)
 
# create the translation matrix using tx and ty, it is a NumPy array 
translation_matrix = np.float32([
        [1, 0, tx], 
        [0, 1, ty]
    ])

# [1 0] and [0 1]:
# These are the identity matrix components that ensure no scaling, rotation, or shearing occurs.
# The 1 in the first row and column represents no horizontal scaling.
# The 1 in the second row and column represents no vertical scaling.

# apply the translation to the image
translated_image = cv2.warpAffine(image, translation_matrix, (width, height)) # cv2.warpAffine(src, M, dsize)

# display the original and the Translated images
cv2.imshow('Translated image', translated_image)
cv2.imshow('Original image', image)
cv2.waitKey(0)
# save the translated image to disk
cv2.imwrite('translated_image.jpg', translated_image)