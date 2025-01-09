import cv2

img = cv2.imread("popy.jpg")

# make a copy of the original image
imageEllipse = img.copy()

height = imageEllipse.shape[0]
width = imageEllipse.shape[1]
# define the center point of ellipse
ellipse_center = (int(width/2), int(height/2))
# define the major and minor axes of the ellipse
axis1 = (200, 50)
axis2 = (125, 125)
# draw the ellipse
# ellipse(image, centerCoordinates, axesLength, angle, startAngle, endAngle, color, thickness) # angle = orientation
#Horizontal
cv2.ellipse(imageEllipse, ellipse_center, axis1, 0, 0, 360, (255, 255, 0), thickness=3)
#Vertical
cv2.ellipse(imageEllipse, ellipse_center, axis2, 90, 0, 360, (0, 0, 255), thickness=3)
# display the output
cv2.imshow('ellipse Image',imageEllipse)
cv2.waitKey(0)