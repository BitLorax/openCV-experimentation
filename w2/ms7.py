
import cv2
import numpy as np
import os


def increaseContrast(img):
    minVal = np.min(img[np.nonzero(img)])
    img[np.nonzero(img)] = img[np.nonzero(img)] - (minVal - 1)
    maxVal = np.max(img[np.nonzero(img)])
    img[np.nonzero(img)] = img[np.nonzero(img)] * (255 / maxVal)
    return img


# current parameters work best with CardsAndSigns
# this works best on Exit1.jpg; need to adjust threshold for colored signs
def findCorners(img):
    res = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    res = cv2.GaussianBlur(res, (11, 11), 0)
    _, res = cv2.threshold(res, 150, 255, cv2.THRESH_TOZERO)
    res = increaseContrast(res)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
    res = cv2.erode(res, kernel, iterations=1)
    for i in range(0, 3):
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (27, 27))
        res = cv2.morphologyEx(res, cv2.MORPH_CLOSE, kernel)

    feats = cv2.goodFeaturesToTrack(res, 100, .1, 5)
    feats = np.int0(feats)
    STImg = img
    for i in feats:
        x, y = i.ravel()
        cv2.circle(STImg, (x, y), 5, (0, 255, 0), -1)

    cv2.imshow("Gray", res)
    cv2.imshow("Result", STImg)

    # fast = cv2.FastFeatureDetector_create()
    # keypts = fast.detect(img, None)
    # fastImg = cv2.drawKeypoints(blurImg, keypts, None, (255, 0, 0), 4)
    # cv2.imshow("FAST", fastImg)


for file in os.listdir("../SampleImages/CardsAndSigns"):
    img = cv2.imread("../SampleImages/CardsAndSigns/" + file)
    findCorners(img)
    cv2.waitKey()

# vidCap = cv2.VideoCapture(0)
# ct = 0
# while (True):
#     ret, img = vidCap.read()
#     if (not ret): break
#     findCorners(img)
#     k = chr(cv2.waitKey(20) & 0xFF)
#     if (k == "q"): break

'''
Shi-Tomasi works better on any given picture because it has parameters that we
can tweak around with to get better results. FAST (to my knowledge) doesn't
have custom configurations.
I'm not sure which one would work better over a set of pictures; I'm guessing
they will perform similarly. If the pictures are similar, though, maybe
Shi-Tomasi would work better with its tweaked parameters.
'''
