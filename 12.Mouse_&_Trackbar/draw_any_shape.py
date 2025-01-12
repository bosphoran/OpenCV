import cv2

# Initialize global variables
drawing = True
start_point = None

# Mouse callback function
def handle_mouse(event, x, y, flags, param):
    global drawing, start_point, image

    if event == cv2.EVENT_LBUTTONDOWN:
        if start_point is not None:
            # Draw a red line from the last starting point to the current point
            cv2.line(image, start_point, (x, y), (0, 0, 255), 2)  # Red color, thickness=2
        # Update the starting point
        start_point = (x, y)
        print(f"Start Point updated to: {start_point}")

    elif event == cv2.EVENT_RBUTTONDOWN:
        # Stop drawing when the right mouse button is clicked
        drawing = False
        print("Stopped drawing.")

# Read an image
image = cv2.imread("mouse.jpg")

# Create a window and set the mouse callback
cv2.namedWindow("Image")
cv2.setMouseCallback("Image", handle_mouse)

while True:
    # Display the image
    cv2.imshow("Image", image)

    # Exit the loop if 'q' is pressed or if drawing is stopped
    if cv2.waitKey(1) & 0xFF == ord('q') or not drawing:
        break

# Close all OpenCV windows
cv2.destroyAllWindows()
