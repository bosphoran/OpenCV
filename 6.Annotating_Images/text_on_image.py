import cv2

img = cv2.imread("popy.jpg")

# make a copy of the original image
imageText = img.copy()
#let's write the text you want to put on the image
text = 'I am a Happy Popy!'
#org: Where you want to put the text. starting location for the top left corner of the text string.
org = (50, 350)
# write the text on the input image
cv2.putText(imageText, text, org, fontFace = 4, fontScale = 1.5, color = (255, 225, 0))
# display the output image with text over it
cv2.imshow("Image Text", imageText)
cv2.imwrite("textedImage.jpg", imageText)
cv2.waitKey(0)
cv2.destroyAllWindows()

# fontFace = cv2.FONT_HERSHEY_COMPLEX
#   FONT_HERSHEY_SIMPLEX        = 0,
#   FONT_HERSHEY_PLAIN          = 1,
#   FONT_HERSHEY_DUPLEX         = 2,
#   FONT_HERSHEY_COMPLEX        = 3,
#   FONT_HERSHEY_TRIPLEX        = 4,
#   FONT_HERSHEY_COMPLEX_SMALL  = 5,
#   FONT_HERSHEY_SCRIPT_SIMPLEX = 6,
#   FONT_HERSHEY_SCRIPT_COMPLEX = 7,
#   FONT_ITALIC                 = 16