
import cv2
import numpy

vidCap = cv2.VideoCapture(0)

# img1 = cv2.imread("../SampleImages/antiqueTractors.jpg")
# img2 = cv2.imread("../SampleImages/beachBahamas.jpg")
# _, img2 = vidCap.read()
# (h1, w1, d1) = img1.shape
# (h2, w2, d2) = img2.shape
# img1 = img1[0:min(h1, h2), 0:min(w1, w2)]
# img2 = img2[0:min(h1, h2), 0:min(w1, w2)]

# blend = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)

# cv2.imshow("Blend", blend)
# cv2.waitKey()

prev = [(vidCap.read())[1]] * 5
while True:
	ret, img = vidCap.read()
	if (not ret): break
	cv2.imshow("Blend", cv2.addWeighted(prev[2], 0.7, cv2.addWeighted(prev[1], 0.7, cv2.addWeighted(prev[0], 0.7, img, 0.3, 0), 0.3, 0), 0.3, 0))
	k = chr(cv2.waitKey(20) & 0xFF)
	if (k == "q"): break
	prev.append(img)
	prev.pop(0)

