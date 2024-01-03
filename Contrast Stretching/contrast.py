import cv2
import numpy as np

def contrast_stretching(image):
    min_val = np.min(image)
    max_val = np.max(image)

    new_min = 0
    new_max = 255

    stretched_image = ((image - min_val) / (max_val - min_val)) * (new_max - new_min) + new_min

    stretched_image = stretched_image.astype(np.uint8)

    return stretched_image

image = cv2.imread("./Images/images.jpg", cv2.IMREAD_GRAYSCALE)

stretched_image = contrast_stretching(image)

cv2.imshow("Original Image", image)
cv2.imshow("Contrast Stretched Image", stretched_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
