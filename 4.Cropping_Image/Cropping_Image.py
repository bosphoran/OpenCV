# Import packages
import cv2
import numpy as np
 
img = cv2.imread('rose.png')
print(img.shape) # Print image shape
cv2.imshow("original", img)
 
# Cropping an image
cropped_image = img[0:300, 70:370] # img[start_row:end_row, start_col:end_col]
 
# Display cropped image
cv2.imshow("cropped", cropped_image)
 
# Save the cropped image
cv2.imwrite("Image_Cropped.jpg", cropped_image)
 
cv2.waitKey(0)
cv2.destroyAllWindows()