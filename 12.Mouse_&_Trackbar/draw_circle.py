import cv2

# Initialize global variables
drawing = False
start_point = (0, 0)
end_point = (0, 0)

# Mouse callback function
def draw_circle(event, x, y, flags, param):
    global drawing, start_point, end_point

    if event == cv2.EVENT_LBUTTONDOWN:
        # Record the starting point and set the drawing flag to True
        drawing = True
        start_point = (x, y)

    elif event == cv2.EVENT_LBUTTONUP:
        # Record the ending point, set the drawing flag to False
        drawing = False
        end_point = (x, y)
        
        # Calculate the radius
        radius = int(((start_point[0] - end_point[0]) ** 2 + (start_point[1] - end_point[1]) ** 2) ** 0.5)
        
        # Draw the circle on the image
        cv2.circle(image, start_point, radius, (0, 255, 0), 2)

# Read an image
image = cv2.imread("mouse.jpg")

# Create a window and set the mouse callback
cv2.namedWindow("Image")
cv2.setMouseCallback("Image", draw_circle)
# cv2.setMouseCallback() function binds the draw_circle() function to mouse events in the window.

while True:
    # Display the image
    cv2.imshow("Image", image)
    
    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Close all OpenCV windows
cv2.destroyAllWindows()
