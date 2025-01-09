import cv2

img = cv2.imread("popy.jpg")

# make a copy of the original image
imageRectangle = img.copy()

height = imageRectangle.shape[0]
width = imageRectangle.shape[1]
# define the starting and end points of the rectangle
start_point =(int(width/2), int(height/5))
end_point =(int(width - 120), int(height - 40))
# draw the rectangle
cv2.rectangle(imageRectangle, start_point, end_point, (255, 255, 0), thickness=3, lineType=cv2.LINE_8) 
# display the output
cv2.imshow('imageRectangle', imageRectangle)
cv2.imwrite("rectangled.jpg", imageRectangle)
cv2.waitKey(0)