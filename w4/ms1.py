
import cv2
cam = cv2.VideoCapture(0)
ret, prevFrame = cam.read()
prevFrame = cv2.cvtColor(prevFrame, cv2.COLOR_BGR2GRAY)

while True:
    ret, currFrame = cam.read()
    gray = cv2.cvtColor(currFrame, cv2.COLOR_BGR2GRAY)
    diff = cv2.absdiff(prevFrame, gray)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    diff = cv2.morphologyEx(diff, cv2.MORPH_OPEN, kernel)
    _, diff = cv2.threshold(diff, 50, 255, cv2.THRESH_BINARY)
    contrs, hier = cv2.findContours(diff, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(currFrame, contrs, -1, (0, 255, 0), 3)
    cv2.imshow("Motion", currFrame)
    x = cv2.waitKey(20)
    c = chr(x & 0xFF)
    if c == "q":
        break
    prevFrame = gray

cam.release()
cv2.destroyAllWindows()

# I tried to tune the parameters so that this finds one complete contour
# but couldn't get it to work perfectly. Right now it's showing a bunch of
# broken up contours that together makes an outline of the moving object
