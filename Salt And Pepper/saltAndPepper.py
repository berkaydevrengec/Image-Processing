import cv2
import numpy as np
import matplotlib.pyplot as plt

def add_salt_and_pepper_noise(image, salt_prob, pepper_prob):
    noisy_image = image.copy()

    total_pixels = image.size
    num_salt = int(total_pixels * salt_prob)
    salt_coords = [np.random.randint(0, i - 1, num_salt) for i in image.shape]
    noisy_image[salt_coords] = 255  # 255: Beyaz renk

    num_pepper = int(total_pixels * pepper_prob)
    pepper_coords = [np.random.randint(0, i - 1, num_pepper) for i in image.shape]
    noisy_image[pepper_coords] = 0  # 0: Siyah renk

    return noisy_image

# Örnek bir görüntüyü yükleme
image = cv2.imread("./Images/lena.jpg", cv2.IMREAD_GRAYSCALE)

# Salt-and-pepper gürültüsü eklenmiş görüntüyü oluşturma
salt_and_pepper_prob = 0.02  # Salt ve pepper olasılıkları
noisy_image = add_salt_and_pepper_noise(image, salt_and_pepper_prob, salt_and_pepper_prob)

# Orijinal ve salt-and-pepper gürültüsü eklenmiş görüntüleri gösterme
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title("Original Image")

plt.subplot(1, 2, 2)
plt.imshow(noisy_image, cmap='gray')
plt.title("Image with Salt-and-Pepper Noise")

plt.show()
