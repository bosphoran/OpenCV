import cv2

img = cv2.imread('popy.jpg')
cv2.imshow('Original Image',img)
cv2.waitKey(0)

# Print error message if image is null
if img is None:
    print('Could not read image')

# Draw line on image
imageLine = img.copy()
height = imageLine.shape[0]
width = imageLine.shape[1]
# Draw the image from point A to B
pointA = (int(width/2), 0) # A(x1, y1)
pointB = (int(width/2), height) # B(x2, y2)
lineColor = (255, 255, 0) # GBR
thickness = 3
lineType = cv2.LINE_AA
cv2.line(imageLine, pointA, pointB, lineColor, thickness, lineType) # line(image, start_point, end_point, color, thickness)

cv2.imshow('Image Line', imageLine)
cv2.imwrite('annotated.jpg', imageLine)
cv2.waitKey(0)