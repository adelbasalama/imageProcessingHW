import cv2
import numpy as np
import matplotlib.pyplot as plt

def apply_gaussian_blur(image, blur_kernel_size):
    blurred_image = cv2.GaussianBlur(image, (blur_kernel_size, blur_kernel_size), 0)
    return blurred_image

def apply_sharpening(image, sharpening_factor):
    sharpening_kernel = np.array([[-1, -1, -1],
                                  [-1,  9, -1],
                                  [-1, -1, -1]])

    sharpened_image = cv2.filter2D(image, -1, sharpening_factor * sharpening_kernel)
    return sharpened_image

image_path = 'Photos/Cat.jpg'
original_image = cv2.imread(image_path)

plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.show()

blur_kernel_size = 5
smoothed_image = apply_gaussian_blur(original_image, blur_kernel_size)

plt.imshow(cv2.cvtColor(smoothed_image, cv2.COLOR_BGR2RGB))
plt.title(f'Smoothed Image (Blur Kernel Size: {blur_kernel_size})')
plt.show()

sharpening_factor = 1.5
sharpened_image = apply_sharpening(smoothed_image, sharpening_factor)

plt.imshow(cv2.cvtColor(sharpened_image, cv2.COLOR_BGR2RGB))
plt.title(f'Sharpened Image (Sharpening Factor: {sharpening_factor})')
plt.show()
