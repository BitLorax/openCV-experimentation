
import os
import cv2

imageNames = os.listdir("../SampleImages") # I have ".." bc of the way I organized my code

for img in imageNames:
	if (not(img.endswith("jpg") or img.endswith("png"))): continue
	cv2img = cv2.imread("../SampleImages/" + img)
	cv2.imshow("Images", cv2img)
	cv2.waitKey()
