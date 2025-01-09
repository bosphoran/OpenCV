import cv2

# Open webcam feed
webcam_cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Define the codec and create VideoWriter object
video_path = 'mywebcam.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for MP4 files
# Obtain frame size information using get() method
CAP_PROP_FRAME_WIDTH = 640
CAP_PROP_FRAME_HEIGHT = 480
frame_width = int(webcam_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(webcam_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


frame_size = (frame_width, frame_height)
fps = 20

output = cv2.VideoWriter(video_path, fourcc, fps, frame_size)

while(webcam_cap.isOpened()):
    # webcam_cap.read() methods returns a tuple, first element is a bool and the second is frame
 
    ret, frame = webcam_cap.read()
    if ret == True:
        # Write the frame to the output file
        output.write(frame)
        # Optionally display the frame
        cv2.imshow('Webcam', frame)

        # Break on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print('Stream disconnected')
        break
           
# Release the objects
webcam_cap.release()
output.release()
cv2.destroyAllWindows()

# The cv2.waitKey(1) waits for a key press and returns the ASCII value of the pressed key (masked with & 0xFF).
# The result is compared to ord('q') (the ASCII value of 'q').
