import cv2
import numpy as np

def laplacian_filter(image):
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    laplacian = cv2.Laplacian(image, cv2.CV_64F)

    laplacian = np.abs(laplacian)

    laplacian = laplacian.astype(np.uint8)

    return laplacian

image = cv2.imread("./Images/example_image.jpg")

filtered_image = laplacian_filter(image)

cv2.imshow("Original Image", image)
cv2.imshow("Filtered Image (Laplace Filter)", filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
