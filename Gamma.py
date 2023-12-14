import cv2
import numpy as np
import matplotlib.pyplot as plt

def adjust_gamma(image, gamma):
    gamma_corrected = np.clip(image ** (1/gamma), 0, 255).astype(np.uint8)
    return gamma_corrected

image_path = 'Photos/Cat.jpg'
original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

plt.imshow(original_image, cmap='gray')
plt.title('Original Image')
plt.show()

gamma_value = 1.5
gamma_corrected_image = adjust_gamma(original_image, gamma_value)

plt.imshow(gamma_corrected_image, cmap='gray')
plt.title(f'Gamma Corrected Image (Gamma: {gamma_value})')
plt.show()
