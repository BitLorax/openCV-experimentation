
import cv2
import numpy as np
import random

cap = cv2.VideoCapture(0)

dx = 0
dy = 0
ddx = 1
ddy = 1
angle = 0

while (True):
    ret, img = cap.read()
    if (not ret): break
    (height, width, depth) = img.shape
    transMatrix = np.float32([[1, 0, dx], [0, 1, dy]])
    rotMatrix = cv2.getRotationMatrix2D((width / 2, height / 2), angle, 1)
    trans = cv2.warpAffine(img, transMatrix, (width, height))
    trans = cv2.warpAffine(trans, rotMatrix, (width, height))
    cv2.imshow("Cam", trans)
    dx = dx + ddx * 5
    dy = dy + ddy * 5
    if (dx > 200): ddx = -1
    elif (dx < 10): ddx = 1
    if (dy > 200): ddy = -1
    elif (dy < 10): ddy = 1
    angle = (angle + 15 * random.random()) % 360
    print(angle)
    k = chr(cv2.waitKey(20) & 0xFF)
    if (k == "q"): break
