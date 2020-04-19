
import cv2
import numpy

vidCap = cv2.VideoCapture(0)
ct = 0
while (True):
	ret, img = vidCap.read()
	if (not ret): break
	imgF = img[:, ::-1, :]
	cv2.imshow("Cam", imgF)
	k = chr(cv2.waitKey(20) & 0xFF)
	if (k == "q"): break
	elif (k == " "):
		cv2.imwrite(str(ct) + "scrnsht.jpg", img)
		ct = ct + 1
