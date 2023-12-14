import cv2
import numpy as np
import matplotlib.pyplot as plt

def rgb_mean_segmentation(image, threshold):
    mean_values = np.mean(image, axis=(0, 1))

    mask = np.all(image > mean_values * threshold, axis=-1)

    segmented_image = np.zeros_like(image)
    segmented_image[mask] = image[mask]

    return segmented_image

image_path = 'Photos/Cat_1.png'
original_image = cv2.imread(image_path, cv2.IMREAD_COLOR)

plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.show()

threshold = 1.1
segmented_image = rgb_mean_segmentation(original_image, threshold)

plt.imshow(cv2.cvtColor(segmented_image, cv2.COLOR_BGR2RGB))
plt.title(f'Segmented Image (Threshold: {threshold})')
plt.show()
