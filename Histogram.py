import cv2
import numpy as np
import matplotlib.pyplot as plt

def plot_histogram(image):
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])

    plt.plot(hist, color='gray')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    plt.title('Histogram')
    plt.grid(True)
    plt.show()

image_path = 'Photos/Cat.jpg'
original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

plt.imshow(original_image, cmap='gray')
plt.title('Original Image')
plt.show()

plot_histogram(original_image)
