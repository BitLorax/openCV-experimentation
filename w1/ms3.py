
import cv2
import numpy
import random

img = cv2.imread("../SampleImages/antiqueTractors.jpg")
(bc, gc, rc) = cv2.split(img)

# cv2.imshow("Images", cv2.merge((rc, gc, bc)))
# cv2.waitKey()

chns = [bc, gc, rc]
random.shuffle(chns)
cv2.imshow("Images", cv2.merge(chns))
cv2.waitKey()
