import cv2

img = cv2.imread('popy.jpg')
cv2.imshow('Original Image',img)

# Make a copy of image
imageCircle = img.copy()
height = imageCircle.shape[0]
width = imageCircle.shape[1]
# define the center of circle
circle_center = (int(width/2), int(height/2)) # (x1, y1)
# define the radius of the circle
radius = 100
color = (255, 255, 0)
thickness = -1
#  Draw a circle using the circle() Function
cv2.circle(imageCircle, circle_center, radius, color, thickness, lineType=cv2.LINE_AA) 
# Display the result
cv2.imshow("Image Circle",imageCircle)
cv2.imwrite("filled_circled.jpg", imageCircle)
cv2.waitKey(0)