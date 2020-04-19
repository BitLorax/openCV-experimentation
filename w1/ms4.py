
import cv2
import numpy

img = cv2.imread("../SampleImages/snowLeo2.jpg")

cv2.circle(img, (140, 140), 80, (255, 255, 0))
cv2.rectangle(img, (180, 100), (580, 300), (0, 255, 255), -1)
cv2.ellipse(img, (150, 370), (70, 30), 0, 0, 270, (255, 0, 255))
cv2.putText(img, "snowLeo2.jpg", (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))

cv2.imshow("Images", img)
cv2.waitKey()
