import cv2
import numpy as np
import matplotlib.pyplot as plt

def bit_plane_slice(image, bit_position):
    bit_plane = (image >> bit_position) & 1
    bit_plane *= 255
    return bit_plane.astype(np.uint8)

image_path = 'Photos/Cat.jpg'
original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

height, width = original_image.shape

num_bits = 8

plt.figure(figsize=(12, 6))

plt.subplot(3, 3, 1)
plt.imshow(original_image, cmap='gray')
plt.title('Original Image')

for i in range(num_bits):
    plt.subplot(3, 3, i + 2)
    plt.imshow(bit_plane_slice(original_image, i), cmap='gray')
    plt.title(f'Bit Plane {i}')

plt.tight_layout()
plt.show()
