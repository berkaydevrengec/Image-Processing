import cv2
import numpy as np

def average_filter(image, kernel_size):
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    kernel = np.ones((kernel_size, kernel_size), np.float32) / (kernel_size * kernel_size)

    filtered_image = cv2.filter2D(image, -1, kernel)

    return filtered_image

image = cv2.imread("./Images/image.jpg")

kernel_size = 5
filtered_image = average_filter(image, kernel_size)

cv2.imshow("Original Image", image)
cv2.imshow("Filtered Image (Average Filter)", filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
