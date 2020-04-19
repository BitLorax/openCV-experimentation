
import cv2

img = cv2.imread("../SampleImages/PuzzlesAndGames/puzzle4.png")

cap = cv2.VideoCapture(0)
orb = cv2.ORB_create()  # some versions use cv2.ORB() instead
fast = cv2.FastFeatureDetector_create()

while (True):
    _, img = cap.read()
    # ORB
    orbKeypts, des = orb.detectAndCompute(img, None)
    orbImg = cv2.drawKeypoints(img, orbKeypts, None, (255, 0, 0), 4)

    # FAST
    fastKeypts = fast.detect(img, None)
    fastImg = cv2.drawKeypoints(img, fastKeypts, None, (255, 0, 0), 4)

    cv2.imshow("ORB", orbImg)
    cv2.imshow("FAST", fastImg)
    k = chr(cv2.waitKey(20) & 0xFF)
    if (k == "q"):
        break  # No noticable difference in speed, both are real-time
