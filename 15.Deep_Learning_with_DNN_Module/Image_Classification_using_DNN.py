# Steps that we will follow while classifying an image.
# 1. Load the class names text file from the disk and extract the required labels.
# 2. Load the pre-trained neural network model from disk.
# 3. Load the image from the disk and prepare the image to be in the correct input format for the deep learning model.
# 4. Forward propagate the input image through the model and obtain the outputs.

import cv2
import numpy as np

# Open the text file containing all the class names in reading mode and split them using each new line.
with open('input/classification_classes_ILSVRC2012.txt', 'r') as f:
   image_net_names = f.read().split('\n')
# [‘tench, Tinca tinca’, ‘goldfish, Carassius auratus’, ‘great white shark, white shark, man-eater, man-eating shark’, ...]

# Split the elements using comma (,) as the delimiter and only keep the first of those elements.
class_names = [name.split(',')[0] for name in image_net_names]
# ['tench', 'goldfish', 'great white shark', 'tiger shark', 'hammerhead', …]


# Load the Pre-Trained DenseNet121 Model from Disk which is trained using the Caffe deep learning framework
model = cv2.dnn.readNet(model='input/DenseNet_121.caffemodel', config='input/DenseNet_121.prototxt', framework='Caffe')

image = cv2.imread("input/lion.jpg")
# create blob from image
blob = cv2.dnn.blobFromImage(image=image, scalefactor=0.01, size=(224, 224), mean=(104, 117, 123))

# Forward Propagate the Input Through the Model:
# Set the input blob for the neural network
model.setInput(blob)
# Forward pass image blog through the model
outputs = model.forward()

# Following block of code reshapes the outputs, after which we can easily get the correct class labels and map the label ID to the class names.
final_outputs = outputs[0]
# make all the outputs 1D
final_outputs = final_outputs.reshape(1000, 1)
# get the class label
label_id = np.argmax(final_outputs)
# convert the output scores to softmax probabilities
probs = np.exp(final_outputs) / np.sum(np.exp(final_outputs))
# get the final highest probability
final_prob = np.max(probs) * 100.
# map the max confidence to the class label names
out_name = class_names[label_id]
out_text = f"{out_name}, {final_prob:.3f}"
# put the class name text on top of the image
cv2.putText(image, out_text, (25, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
cv2.imshow('Image', image)

cv2.waitKey(0)
cv2.imwrite('result_image.jpg', image)