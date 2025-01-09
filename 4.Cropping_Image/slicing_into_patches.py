import cv2
import numpy as np

# Load the image
image = cv2.imread('Image_Cropped.jpg')
height, width, _ = image.shape  # Get image dimensions

# Define the number of patches
num_patches = 4

# Calculate patch size
patch_height = int(height / np.sqrt(num_patches))
patch_width = int(width / np.sqrt(num_patches))

# Adjust the number of patches to be a square grid
rows = int(np.ceil(np.sqrt(num_patches)))
cols = int(np.ceil(num_patches / rows))

# Create patches
patches = []
for i in range(rows):
    for j in range(cols):
        y_start = i * patch_height
        y_end = (i + 1) * patch_height
        x_start = j * patch_width
        x_end = (j + 1) * patch_width

        patch = image[y_start:y_end, x_start:x_end]
        patches.append(patch)

        # Optionally save patches to files
        patch_filename = f'patch_{i}_{j}.jpg'
        cv2.imwrite(patch_filename, patch)

# Display patches (optional)
for idx, patch in enumerate(patches):
    cv2.imshow(f'Patch {idx}', patch)
    cv2.waitKey(0)

cv2.waitKey(0)
cv2.destroyAllWindows()
