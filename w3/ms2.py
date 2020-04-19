import cv2

img1 = cv2.imread("../images/eraser.jpg")
# Using a Pentel eraser, works pretty well in getting detected
# and not detecting other objects

cap = cv2.VideoCapture(0)

while (True):
    _, img2 = cap.read()
    orb = cv2.ORB_create()
    bfMatcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)
    # Find all stable matches
    matches = bfMatcher.match(des1, des2)
    # Sort matches by distance (best matches come first in the list)
    matches.sort(key=lambda x: x.distance)
    # Find index where matches start to be over threshold
    for i in range(len(matches)):
        if matches[i].distance > 35.0:
            break
    # Draw good-quality matches up to the threshold index
    img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:i], None)
    cv2.imshow("Matches", img3)
    k = chr(cv2.waitKey(20) & 0xFF)
    if (k == "q"):
        break
