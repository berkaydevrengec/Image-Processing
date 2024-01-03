'''Normalizasyon:

Amacı, veri değerlerini belirli bir aralığa ölçeklendirmektir (genellikle [0, 1] aralığına).
En küçük değer (min) 0, en büyük değer (max) 1 olacak şekilde dönüştürülür.
Veri dağılımındaki oransal ilişkileri korur.
x_normalized = (x - min) / (max - min)
Standardizasyon:

Amacı, veri değerlerini bir standart normal dağılıma (ortalama = 0, standart sapma = 1) ölçeklendirmektir.
Ortalama değeri çıkartılır ve standart sapmaya bölünür.
Bu yöntem, veri setinin ortalamasını ve varyansını değiştirerek veri setini bir standart forma getirir.
x_standardized = (x - mean) / std'''


import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("./Images/image.jpg", cv2.IMREAD_GRAYSCALE)

normalized_image = (image - np.min(image)) / (np.max(image) - np.min(image))

plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title("Original Image")

plt.subplot(1, 2, 2)
plt.imshow(normalized_image, cmap='gray')
plt.title("Normalized Image")

plt.show()

