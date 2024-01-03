import cv2
import numpy as np
import matplotlib.pyplot as plt

def contraharmonic_mean_filter(image, kernel_size, Q):
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    if kernel_size % 2 == 0:
        raise ValueError("Kernel size should be an odd number.")

    result = np.zeros_like(image, dtype=np.float64)

    for i in range(kernel_size // 2, image.shape[0] - kernel_size // 2):
        for j in range(kernel_size // 2, image.shape[1] - kernel_size // 2):
            roi = image[i - kernel_size // 2:i + kernel_size // 2 + 1, j - kernel_size // 2:j + kernel_size // 2 + 1]
            numerator = np.sum(np.power(roi, Q + 1))
            denominator = np.sum(np.power(roi, Q))
            result[i, j] = numerator / denominator

    result = np.clip(result, 0, 255)
    result = result.astype(np.uint8)

    return result

# Örnek bir görüntüyü yükleme
image = cv2.imread("./Images/image.jpg")

# Contraharmonic Mean filtresi uygulanmış görüntüyü oluşturma
kernel_size = 3
Q = 1.5
filtered_image = contraharmonic_mean_filter(image, kernel_size, Q)

# Orijinal ve filtre uygulanmış görüntüleri gösterme
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")

plt.subplot(1, 2, 2)
plt.imshow(filtered_image, cmap='gray')
plt.title("Contraharmonic Mean Filtered Image (Q={})".format(Q))

plt.show()
