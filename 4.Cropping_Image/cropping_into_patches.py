import cv2
import numpy as np

image = cv2.imread('Image_Cropped.jpg')
cv2.imshow("Original Image", image)

image_copy = image.copy()
height = image.shape[0]
width = image.shape[1]

M = 76
N = 104
x1 = 0
y1 = 0
 
for y in range(0, height, M):
    for x in range(0, width, N):
        if (height - y) < M or (width - x) < N:
            break
             
        y1 = y + M
        x1 = x + N
 
        # check whether the patch width or height exceeds the image width or height
        if x1 >= width and y1 >= height:
            x1 = width - 1
            y1 = height - 1
            #Crop into patches of size MxN
            tiles = image_copy[y:y+M, x:x+N]
            #Save each patch into file directory
            cv2.imwrite('saved_patches/'+'tile'+str(x)+'_'+str(y)+'.jpg', tiles)
            cv2.rectangle(image, (x, y), (x1, y1), (0, 255, 0), 1)
        elif y1 >= height: # when patch height exceeds the image height
            y1 = height - 1
            #Crop into patches of size MxN
            tiles = image_copy[y:y+M, x:x+N]
            #Save each patch into file directory
            cv2.imwrite('saved_patches/'+'tile'+str(x)+'_'+str(y)+'.jpg', tiles)
            cv2.rectangle(image, (x, y), (x1, y1), (0, 255, 0), 1)
        elif x1 >= width: # when patch width exceeds the image width
            x1 = width - 1
            #Crop into patches of size MxN
            tiles = image_copy[y:y+M, x:x+N]
            #Save each patch into file directory
            cv2.imwrite('saved_patches/'+'tile'+str(x)+'_'+str(y)+'.jpg', tiles)
            cv2.rectangle(image, (x, y), (x1, y1), (0, 255, 0), 1)
        else:
            #Crop into patches of size MxN
            tiles = image_copy[y:y+M, x:x+N]
            #Save each patch into file directory
            cv2.imwrite('saved_patches/'+'tile'+str(x)+'_'+str(y)+'.jpg', tiles)
            cv2.rectangle(image, (x, y), (x1, y1), (0, 255, 0), 1)

# Save full image into file directory
cv2.imshow("Patched Image",image)
cv2.imwrite("patched.jpg",image)

cv2.waitKey(0)
cv2.destroyAllWindows()