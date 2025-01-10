import cv2
import numpy as np

image = cv2.imread('wood.jpg')
 
# Print error message if image is null
if image is None:
    print('Could not read image')
    exit()
 
# Apply identity kernel
kernel1 = np.array([[0, 0, 0],
                    [0, 1, 0],
                    [0, 0, 0]])
 
identity = cv2.filter2D(src=image, ddepth=-1, kernel=kernel1)
 
# cv2.imshow('Original', image)
# cv2.imshow('Identity', identity)
     
# cv2.waitKey()
# cv2.imwrite('identity.jpg', identity)
# cv2.destroyAllWindows()
 
# Apply blurring kernel
# Begin by defining a 5×5 kernel, consisting of only ones. 
# Note that we also divide the kernel by 25. Why is that? 
# Well, before you apply any convolution to an image, using a 2D-convolution matrix, you need to ensure that all the values are normalized. 
# This is done by dividing each element of the kernel, by the number of elements in the kernel, which in this case is 25. 
# This ensures all values stay within the range of [0,1], and the total value of the kernel is 1.
kernel2 = np.ones((5, 5), np.float32) / 25
# np.int8: 8-bit signed integer (range: -128 to 127).
# np.uint8: 8-bit unsigned integer (range: 0 to 255).
img = cv2.filter2D(src=image, ddepth=-1, kernel=kernel2)
 
cv2.imshow('Original', image)
cv2.imshow('Kernel Blur', img)

# Built-in Blur function:
img_blur = cv2.blur(src=image, ksize=(5,5)) # Using the blur function to blur an image where ksize is the kernel size
cv2.imshow("Blured using Buil-in Function", img_blur)

# Gaussian blur:
# sigmaX is Gaussian Kernel standard deviation 
# ksize is kernel size
gaussian_blur = cv2.GaussianBlur(src=image, ksize=(5,5), sigmaX=0, sigmaY=0) 
cv2.imshow('Gaussian Blurred', gaussian_blur)

# Median blur:
median = cv2.medianBlur(src=image, ksize=5)
cv2.imshow('Median Blurred', median)

# Apply Bilateral Filtering:
# In bilateralFilter(), d is diameter of each pixel neighborhood that is used during filtering.
# sigmaColor is used to filter sigma in the color space.
# sigmaSpace is used to filter sigma in the coordinate space.
bilateral_filter = cv2.bilateralFilter(src=image, d=9, sigmaColor=75, sigmaSpace=75)
cv2.imshow('Bilateral Filtering', bilateral_filter)
cv2.imwrite('bilateral_filtering.jpg', bilateral_filter)

cv2.waitKey()
cv2.imwrite('blur_kernel.jpg', img)
cv2.destroyAllWindows()



# In image processing, a convolution kernel is a 2D matrix that is used to filter images. 
# Also known as a convolution matrix, a convolution kernel is typically a square, MxN matrix, 
# where both M and N are odd integers (e.g. 3×3, 5×5, 7×7 etc.).

# Convolution of an image with a kernel represents a simple mathematical operation, 
# between the kernel and its corresponding elements in the image.
# 1. Assume that the center of the kernel is positioned over a specific pixel (p), in an image.
# 2. Multiply the value of each element in the kernel with the corresponding pixel element in the source image.
# 3. Now, sum the result of those multiplications and compute the average.
# 4. Finally, replace the value of pixel (p), with the average value you just computed.