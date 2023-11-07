import cv2
import numpy as np

image = cv2.imread("Photos/Cat.jpg")
cv2.imshow("Original", image)


def gaussian_noise(image):
    row, col, ch = image.shape
    mean = 0
    var = 0.05
    sigma = var ** 0.5
    gauss = np.random.normal(mean, sigma, (row, col, ch))
    gauss = gauss.reshape(row, col, ch)
    noisy = image + gauss
    return noisy


img = cv2.imread("Photos/Cat.jpg")
img = img / 255
noise_img = gaussian_noise(img)
cv2.imshow("Gaussian Noise", noise_img)
cv2.waitKey(0)
