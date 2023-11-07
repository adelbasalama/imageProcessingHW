import cv2
import numpy as np


def apply_average_filter(image, kernel_size):
    return cv2.blur(image, (kernel_size, kernel_size))


# Load an image
image_path = 'Photos/Cat.jpg'  # Replace with the actual path to your image
image = cv2.imread(image_path)

# Check if the image was loaded successfully
if image is not None:
    # Define the kernel size (should be an odd number)
    kernel_size = 5  # Adjust this value to change the filter size

    # Apply the average filter
    filtered_image = apply_average_filter(image, kernel_size)

    # Display the original and filtered images
    cv2.imshow('Original Image', image)
    cv2.imshow('Filtered Image', filtered_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Unable to load the image.")
