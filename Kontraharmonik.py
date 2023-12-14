import cv2
import numpy as np
import matplotlib.pyplot as plt

def contraharmonic_mean_filter(image, kernel_size, Q):
    padded_image = cv2.copyMakeBorder(image, kernel_size // 2, kernel_size // 2, kernel_size // 2, kernel_size // 2, cv2.BORDER_CONSTANT)

    filtered_image = np.zeros_like(image, dtype=np.float32)
    for i in range(kernel_size // 2, padded_image.shape[0] - kernel_size // 2):
        for j in range(kernel_size // 2, padded_image.shape[1] - kernel_size // 2):
            region = padded_image[i - kernel_size // 2:i + kernel_size // 2 + 1, j - kernel_size // 2:j + kernel_size // 2 + 1]
            numerator = np.sum(region ** (Q + 1))
            denominator = np.sum(region ** Q)
            filtered_image[i - kernel_size // 2, j - kernel_size // 2] = numerator / denominator if denominator != 0 else 0

    return filtered_image.astype(np.uint8)

image_path = 'Photos/Cat.jpg'
original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

plt.imshow(original_image, cmap='gray')
plt.title('Original Image')
plt.show()

kernel_size = 3
Q = 1.5
filtered_image = contraharmonic_mean_filter(original_image, kernel_size, Q)

plt.imshow(filtered_image, cmap='gray')
plt.title(f'Contraharmonic Mean Filter (Kernel Size: {kernel_size}, Q: {Q})')
plt.show()
