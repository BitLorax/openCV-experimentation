
import cv2

cap = cv2.VideoCapture(0)

MIN_SIZE = 1
MAX_SIZE = 101
blurDir = 2
curBlur = MIN_SIZE

while (True):
    _, img = cap.read()
    height, width, depth = img.shape
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (curBlur, curBlur))
    # blurImg = cv2.GaussianBlur(img, (curBlur, curBlur), 0)
    blurImg = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    cv2.imshow("Cam", blurImg)

    curBlur += blurDir
    if (curBlur == MAX_SIZE or curBlur == MIN_SIZE):
        blurDir = -blurDir

    k = chr(cv2.waitKey(20) & 0xFF)
    if (k == "q"):
        break
