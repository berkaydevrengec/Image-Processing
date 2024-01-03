import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("./Images/image.jpg", cv2.IMREAD_GRAYSCALE)

standardized_image = (image - np.mean(image)) / np.std(image)

plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title("Original Image")

plt.subplot(1, 2, 2)
plt.imshow(standardized_image, cmap='gray')
plt.title("Standardized Image")

plt.show()
