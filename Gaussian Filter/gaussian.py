import cv2
import numpy as np

def gaussian_filter(image, kernel_size, sigma):
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    kernel = cv2.getGaussianKernel(kernel_size, sigma)
    kernel_2d = np.outer(kernel, kernel.transpose())

    filtered_image = cv2.filter2D(image, -1, kernel_2d)

    return filtered_image

image = cv2.imread("./Images/image.png")

kernel_size = 5
sigma = 1.0
filtered_image = gaussian_filter(image, kernel_size, sigma)

cv2.imshow("Original Image", image)
cv2.imshow("Filtered Image (Gaussian Filter)", filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
