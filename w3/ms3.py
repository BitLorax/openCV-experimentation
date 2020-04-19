import cv2
import numpy as np

faceCascade = cv2.CascadeClassifier(
    "../haarCascades/haarcascade_frontalface_alt0.xml")
eyeCascade = cv2.CascadeClassifier(
    "../haarCascades/haarcascade_eye2.xml")
gEye = cv2.imread("../images/GoogleyEye.png")

ratio = .045
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_rects = faceCascade.detectMultiScale(gray, 1.3, 5)
    for (fx, fy, fw, fh) in face_rects:
        roiGray = gray[fy:fy+fh, fx:fx+fw]
        roiFrame = frame[fy:fy+fh, fx:fx+fw]
        eye_rects = eyeCascade.detectMultiScale(roiGray)

        # filter by position
        use = []
        for (ex, ey, ew, eh) in eye_rects:
            if (ey < (2 * fh / 5)):
                use.append((ex, ey, ew, eh))
        eye_rects = np.array(use)

        # filter by area ratio
        scores = []
        i = 0
        for (ex, ey, ew, eh) in eye_rects:
            scores.append((abs(ew * eh / (fw * fh) - ratio), i))
            i = i + 1
        scores.sort()

        i = 0
        for (ex, ey, ew, eh) in eye_rects:
            if (len(scores) >= 2):
                if (scores[-1][1] != i and scores[-2][1] != i):
                    continue
            center = (int(ex+ew/2), int(ey+eh/2))
            rad = int(.3 * (ew + eh))
            curGEye = cv2.resize(gEye, (ew, eh))
            grayCurGEye = cv2.cvtColor(curGEye, cv2.COLOR_BGR2GRAY)
            _, mask = cv2.threshold(grayCurGEye, 250, 255,
                                    cv2.THRESH_BINARY_INV)
            maskedFrame = cv2.bitwise_and(roiFrame[ey:ey+eh, ex:ex+ew],
                                          roiFrame[ey:ey+eh, ex:ex+ew],
                                          mask=~mask)
            maskedEye = cv2.bitwise_and(curGEye, curGEye, mask=mask)
            roiFrame[ey:ey+eh, ex:ex+ew] = cv2.add(maskedFrame, maskedEye)
            i = i + 1
    cv2.imshow("Cam", frame)
    v = cv2.waitKey(50)
    c = chr(v & 0xFF)
    if c == 'q':
        break

cap.release()
cv2.destroyAllWindows()
