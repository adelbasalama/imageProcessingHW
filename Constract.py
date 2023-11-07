import cv2


def adjust_contrast(image, alpha, beta):
    # Apply contrast adjustment
    adjusted_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    return adjusted_image


# Load an image
image_path = 'Photos/Cat.jpg'  # Replace with the actual path to your image
image = cv2.imread(image_path)

# Check if the image was loaded successfully
if image is not None:
    # Increase contrast (alpha > 1 increases contrast, beta shifts brightness)
    adjusted_image = adjust_contrast(image, alpha=2.0, beta=0)

    # Display the original and adjusted images
    cv2.imshow('Original Image', image)
    cv2.imshow('Adjusted Image', adjusted_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Unable to load the image.")
