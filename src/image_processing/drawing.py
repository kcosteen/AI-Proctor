import cv2

image = cv2.imread("my_photo.jpg")

# Draw rectangle
cv2.rectangle(
    image,
    (50, 50),
    (250, 200),
    (0, 255, 0),
    3
)

# Draw circle
cv2.circle(
    image,
    (150, 300),
    50,
    (255, 0, 0),
    3
)

# Add text
cv2.putText(
    image,
    "AI Proctor",
    (50, 400),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (0, 0, 255),
    2
)

cv2.imshow("Drawing", image)

cv2.waitKey(0)
cv2.destroyAllWindows()