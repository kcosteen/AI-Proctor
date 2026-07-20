import cv2

image = cv2.imread("my_photo.jpg")

# Apply blur
blur = cv2.GaussianBlur(
    image,
    (15, 15),
    0
)

cv2.imshow("Original", image)
cv2.imshow("Blur", blur)

cv2.waitKey(0)
cv2.destroyAllWindows()