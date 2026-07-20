import cv2

image = cv2.imread("my_photo.jpg")

# Convert to grayscale
gray = cv2.cvtColor(
    image,
    cv2.COLOR_BGR2GRAY
)

# Apply threshold
_, threshold = cv2.threshold(
    gray,
    127,
    255,
    cv2.THRESH_BINARY
)

cv2.imshow("Grayscale", gray)
cv2.imshow("Threshold", threshold)

cv2.waitKey(0)
cv2.destroyAllWindows()