import cv2

# Load the video
vid_capture = cv2.VideoCapture('Jim_Rohn.mp4')

# Check if the video opened successfully
if not vid_capture.isOpened():
    print("Error: Could not open video.")
    exit()

# Set the frame position to the desired frame (e.g., frame 50)
frame_number = 200
vid_capture.set(cv2.CAP_PROP_POS_FRAMES, frame_number)

# Read the frame
success, frame = vid_capture.read()

if success:
    # Save the frame as an image
    output_filename = f'frame_{frame_number}.jpg'
    cv2.imwrite(output_filename, frame)
    print(f"Frame {frame_number} saved as {output_filename}.")
else:
    print(f"Error: Could not read frame {frame_number}.")

# Release the video capture object
vid_capture.release()
