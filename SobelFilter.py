import cv2
import numpy as np
import matplotlib.pyplot as plt

def apply_sobel_filter(image):
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

    gradient_magnitude = np.sqrt(sobel_x**2 + sobel_y**2)

    gradient_magnitude = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX)

    return gradient_magnitude.astype(np.uint8)

image_path = 'Photos/Cat.jpg'
original_image = cv2.imread(image_path)

plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.show()

sobel_filtered_image = apply_sobel_filter(original_image)

plt.imshow(sobel_filtered_image, cmap='gray')
plt.title('Sobel Filtered Image')
plt.show()
