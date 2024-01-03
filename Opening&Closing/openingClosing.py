import cv2
import numpy as np
import matplotlib.pyplot as plt

def apply_morphological_operations(image, operation_type, kernel_size):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))

    if operation_type == 'opening':
        result = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
    elif operation_type == 'closing':
        result = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    else:
        raise ValueError("Invalid operation type. Use 'opening' or 'closing'.")

    return result

image = cv2.imread("./Images/image.jpg", cv2.IMREAD_GRAYSCALE)

opening_result = apply_morphological_operations(image, 'opening', kernel_size=5)

closing_result = apply_morphological_operations(image, 'closing', kernel_size=5)

plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.imshow(image, cmap='gray')
plt.title("Original Image")

plt.subplot(1, 3, 2)
plt.imshow(opening_result, cmap='gray')
plt.title("Opening Result")

plt.subplot(1, 3, 3)
plt.imshow(closing_result, cmap='gray')
plt.title("Closing Result")

plt.show()
