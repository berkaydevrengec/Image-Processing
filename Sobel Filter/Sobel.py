import cv2 

img = cv2.imread("./Images/p.png")

sobel_horizontal = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobel_vertical = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

cv2.imshow("horizontal",sobel_horizontal)
cv2.imshow("vertical",sobel_vertical)

cv2.waitKey(0)
cv2.destroyAllWindows()
