import cv2
import numpy as np
import matplotlib.pyplot as plt

def perform_morphological_operations(image, operation_type, kernel_size):
    kernel = np.ones((kernel_size, kernel_size), np.uint8)

    if operation_type == 'opening':
        result_image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
    elif operation_type == 'closing':
        result_image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    else:
        raise ValueError("Invalid operation type. Use 'opening' or 'closing'.")

    return result_image

image_path = 'Photos/Cat.jpg'
binary_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

plt.imshow(binary_image, cmap='gray')
plt.title('Original Image')
plt.show()

opening_result = perform_morphological_operations(binary_image, 'opening', kernel_size=5)

plt.imshow(opening_result, cmap='gray')
plt.title('Opening Operation Result')
plt.show()

closing_result = perform_morphological_operations(binary_image, 'closing', kernel_size=5)

plt.imshow(closing_result, cmap='gray')
plt.title('Closing Operation Result')
plt.show()
