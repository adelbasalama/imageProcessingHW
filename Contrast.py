import cv2
import numpy as np
import matplotlib.pyplot as plt

def adjust_contrast(image, alpha):
    adjusted_image = np.clip(alpha * image, 0, 255).astype(np.uint8)
    return adjusted_image

image_path = 'Photos/Cat.jpg'
original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

plt.imshow(original_image, cmap='gray')
plt.title('Original Image')
plt.show()

contrast_factor = 1.5
contrast_adjusted_image = adjust_contrast(original_image, contrast_factor)

plt.imshow(contrast_adjusted_image, cmap='gray')
plt.title(f'Contrast Adjusted Image (Factor: {contrast_factor})')
plt.show()
