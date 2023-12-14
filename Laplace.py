import cv2
import numpy as np
import matplotlib.pyplot as plt

def apply_blur_and_laplacian(image, blur_kernel_size):
    blurred_image = cv2.GaussianBlur(image, (blur_kernel_size, blur_kernel_size), 0)

    laplacian = cv2.Laplacian(blurred_image, cv2.CV_64F)

    laplacian = cv2.normalize(laplacian, None, 0, 255, cv2.NORM_MINMAX)

    return laplacian.astype(np.uint8)

image_path = 'Photos/Cat.jpg'
original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

plt.imshow(original_image, cmap='gray')
plt.title('Original Image')
plt.show()

blur_kernel_size = 5
laplacian_filtered_image = apply_blur_and_laplacian(original_image, blur_kernel_size)

plt.imshow(laplacian_filtered_image, cmap='gray')
plt.title(f'Blurring with Laplacian (Blur Kernel Size: {blur_kernel_size})')
plt.show()
