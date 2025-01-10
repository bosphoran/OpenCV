import cv2
import numpy as np
bright = cv2.imread('bright.png')
dark = cv2.imread('dark.png')

# The LAB Color-Space:
# L – Lightness ( Intensity ).
# a – color component ranging from Green to Magenta.
# b – color component ranging from Blue to Yellow.
# the L channel encodes brightness only. The other two channels encode color.
brightLAB = cv2.cvtColor(bright, cv2.COLOR_BGR2LAB)
darkLAB = cv2.cvtColor(dark, cv2.COLOR_BGR2LAB)
# cv2.imshow('BGR2LAB Bright', brightLAB)
# cv2.imshow('BGR2LAB Dark', darkLAB)

# The YCrCb Color-Space:
# Y – Luminance or Luma component obtained from RGB after gamma correction.
# Cr = R – Y ( how far is the red component from Luma ).
# Cb = B – Y ( how far is the blue component from Luma ).
brightYCB = cv2.cvtColor(bright, cv2.COLOR_BGR2YCrCb)
darkYCB = cv2.cvtColor(dark, cv2.COLOR_BGR2YCrCb)
# cv2.imshow('BGR2YCrCb Bright', brightYCB)
# cv2.imshow('BGR2YCrCb Dark', darkYCB)

# The HSV Color Space:
# H – Hue ( Dominant Wavelength ).
# S – Saturation ( Purity / shades of the color ).
# V – Value ( Intensity ).
# it uses only one channel to describe color (H)
brightHSV = cv2.cvtColor(bright, cv2.COLOR_BGR2HSV)
darkHSV = cv2.cvtColor(dark, cv2.COLOR_BGR2HSV)

# Applying threshold for segmentation:
# Extract all pixels from the image which have values close to that of the green pixel. 
# We can take a range of +/- 40 for each color space and check how the results look like. 
# We will use the opencv function inRange for finding the mask of green pixels and 
# then use bitwise_and operation to get the green pixels from the image using the mask.

# for converting one pixel to another color space, we first need to convert 1D array to a 3D array.
bgr = [40, 158, 16]
thresh = 40
 
minBGR = np.array([bgr[0] - thresh, bgr[1] - thresh, bgr[2] - thresh])
maxBGR = np.array([bgr[0] + thresh, bgr[1] + thresh, bgr[2] + thresh])
 
maskBGR = cv2.inRange(bright,minBGR,maxBGR)
resultBGR = cv2.bitwise_and(bright, bright, mask = maskBGR)
 
#convert 1D array to 3D, then convert it to HSV and take the first element
# this will be same as shown in the above figure [65, 229, 158]
hsv = cv2.cvtColor( np.uint8([[bgr]] ), cv2.COLOR_BGR2HSV)[0][0]
 
minHSV = np.array([hsv[0] - thresh, hsv[1] - thresh, hsv[2] - thresh])
maxHSV = np.array([hsv[0] + thresh, hsv[1] + thresh, hsv[2] + thresh])
 
maskHSV = cv2.inRange(brightHSV, minHSV, maxHSV)
resultHSV = cv2.bitwise_and(brightHSV, brightHSV, mask = maskHSV)
 
#convert 1D array to 3D, then convert it to YCrCb and take the first element
ycb = cv2.cvtColor( np.uint8([[bgr]] ), cv2.COLOR_BGR2YCrCb)[0][0]
 
minYCB = np.array([ycb[0] - thresh, ycb[1] - thresh, ycb[2] - thresh])
maxYCB = np.array([ycb[0] + thresh, ycb[1] + thresh, ycb[2] + thresh])
 
maskYCB = cv2.inRange(brightYCB, minYCB, maxYCB)
resultYCB = cv2.bitwise_and(brightYCB, brightYCB, mask = maskYCB)
 
#convert 1D array to 3D, then convert it to LAB and take the first element
lab = cv2.cvtColor( np.uint8([[bgr]] ), cv2.COLOR_BGR2LAB)[0][0]
 
minLAB = np.array([lab[0] - thresh, lab[1] - thresh, lab[2] - thresh])
maxLAB = np.array([lab[0] + thresh, lab[1] + thresh, lab[2] + thresh])
 
maskLAB = cv2.inRange(brightLAB, minLAB, maxLAB)
resultLAB = cv2.bitwise_and(brightLAB, brightLAB, mask = maskLAB)
 
cv2.imshow("Result BGR", resultBGR)
cv2.imshow("Result HSV", resultHSV)
cv2.imshow("Result YCB", resultYCB)
cv2.imshow("Output LAB", resultLAB)

cv2.waitKey(0)
cv2.destroyAllWindows()