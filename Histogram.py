import cv2
import matplotlib.pyplot as plt

def plot_histogram(image):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Calculate histograms for each channel (R, G, B) and grayscale
    color_histograms = [cv2.calcHist([image], [i], None, [256], [0, 256]) for i in range(3)]
    gray_histogram = cv2.calcHist([gray_image], [0], None, [256], [0, 256])

    # Plot histograms
    colors = ['b', 'g', 'r']
    labels = ['Blue', 'Green', 'Red', 'Grayscale']
    histograms = color_histograms + [gray_histogram]

    for i, histogram in enumerate(histograms):
        plt.plot(histogram, color=colors[i-1])
        plt.xlim([0, 256])

    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.title('Histogram')
    plt.legend(labels)
    plt.show()

# Load an image
image_path = 'Photos/Cat.jpg'  # Replace with the actual path to your image
image = cv2.imread(image_path)

# Check if the image was loaded successfully
if image is not None:
    plot_histogram(image)
else:
    print("Error: Unable to load the image.")
