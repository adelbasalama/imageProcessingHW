import cv2
import numpy as np
import matplotlib.pyplot as plt

def apply_average_filter(image, kernel_size):
    kernel = np.ones((kernel_size, kernel_size), np.float32) / (kernel_size ** 2)

    filtered_image = cv2.filter2D(image, -1, kernel)

    return filtered_image

image_path = 'Photos/Cat.jpg'
original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

plt.imshow(original_image, cmap='gray')
plt.title('Original Image')
plt.show()

kernel_size = 5
filtered_image = apply_average_filter(original_image, kernel_size)

plt.imshow(filtered_image, cmap='gray')
plt.title(f'Average Filtered Image (Kernel Size: {kernel_size})')
plt.show()
