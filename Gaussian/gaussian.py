import cv2
import numpy as np
import matplotlib.pyplot as plt

def apply_gaussian(image, sigma):
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    gaussian_filtered_image = cv2.GaussianBlur(image, (0, 0), sigma)

    return gaussian_filtered_image

image = cv2.imread("./Images/image.jpg")

sigma = 1.5
gaussian_filtered_image = apply_gaussian(image, sigma)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")

plt.subplot(1, 2, 2)
plt.imshow(gaussian_filtered_image, cmap='gray')
plt.title("Gaussian Filtered Image (Sigma = {})".format(sigma))

plt.show()
