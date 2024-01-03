import cv2
import numpy as np
import matplotlib.pyplot as plt

def smoothing(image):
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    smoothed_image = cv2.blur(image, (3, 3))

    return smoothed_image

def sharpening(image):
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    laplacian = cv2.Laplacian(image, cv2.CV_64F)

    laplacian = np.abs(laplacian)

    laplacian = laplacian.astype(np.uint8)

    sharpened_image = cv2.addWeighted(image, 1.5, laplacian, -0.5, 0)

    return sharpened_image

image = cv2.imread("./Images/image.jpg")

original_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
smoothed_image = smoothing(image)
sharpened_image = sharpening(image)

plt.figure(figsize=(10, 7))

plt.subplot(1, 3, 1)
plt.imshow(original_image)
plt.title("Original Image")

plt.subplot(1, 3, 2)
plt.imshow(smoothed_image, cmap='gray')
plt.title("Smoothed Image")

plt.subplot(1, 3, 3)
plt.imshow(sharpened_image, cmap='gray')
plt.title("Sharpened Image")

plt.show()
