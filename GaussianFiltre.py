import cv2
import numpy as np
import matplotlib.pyplot as plt

def apply_gaussian_filter(image, kernel_size, sigma):
    filtered_image = cv2.GaussianBlur(image, (kernel_size, kernel_size), sigma)

    return filtered_image

image_path = 'Photos/Cat.jpg'
original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

plt.imshow(original_image, cmap='gray')
plt.title('Original Image')
plt.show()

kernel_size = 5
sigma = 1.0
filtered_image = apply_gaussian_filter(original_image, kernel_size, sigma)

plt.imshow(filtered_image, cmap='gray')
plt.title(f'Gaussian Filtered Image (Kernel Size: {kernel_size}, Sigma: {sigma})')
plt.show()
