import cv2
import matplotlib.pyplot as plt

image = cv2.imread("./Images/image.jpg")

blue, green, red = cv2.split(image)

plt.figure(figsize=(12, 4))

plt.subplot(1, 4, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")

plt.subplot(1, 4, 2)
plt.imshow(red, cmap='gray')
plt.title("Red Channel")

plt.subplot(1, 4, 3)
plt.imshow(green, cmap='gray')
plt.title("Green Channel")

plt.subplot(1, 4, 4)
plt.imshow(blue, cmap='gray')
plt.title("Blue Channel")

plt.show()
