import cv2

image = cv2.imread("my_photo.jpg")

# Resize image
small_image = cv2.resize(image, (320, 240))

# Display original and resized images
cv2.imshow("Original", image)
cv2.imshow("Small Image", small_image)

cv2.waitKey(0)

cv2.destroyAllWindows()