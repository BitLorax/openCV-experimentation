
import cv2

im1 = cv2.imread("../SampleImages/antiqueTractors.jpg")
im2 = cv2.imread("../SampleImages/beachBahamas.jpg")
im3 = cv2.imread("../SampleImages/canyonlands.jpg")
im4 = cv2.imread("../SampleImages/chicago.jpg")

cv2.imshow("Images", im1)
cv2.waitKey()
cv2.imshow("Images", im2)
cv2.waitKey()
cv2.imshow("Images", im3)
cv2.waitKey()
cv2.imshow("Images", im4)
cv2.waitKey()
