
import cv2
import numpy as np

ul = None
ll = None
ur = None


def mouseResponse(event, x, y, flags, param):
    """This function is a callback that happens when the mouse is used.
    event describes which mouse event triggered the callback, (x, y) is
    the location in the window where the event happened. The other inputs
    may be ignored."""
    global ul, ll, ur
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(workImg, (x, y), 5, (255, 0, 255), -1)
        if (ul is None): ul = [x, y]
        elif (ll is None): ll = [x, y]
        elif (ur is None): ur = [x, y]


# read in an image
img = cv2.imread("../SampleImages/CardsAndSigns/Pink3.jpg")
height, width, depth = img.shape

# make a copy and set up the window to display it
workImg = img.copy()
cv2.namedWindow("Working image")

# assign mouse_response to be the callback function for the Working image window
cv2.setMouseCallback("Working image", mouseResponse)

# Keep re-displaying the window, and look for user to type 'q' to quit
while True:
    cv2.imshow("Working image", workImg)
    x = cv2.waitKey(20)
    if (ul is not None and ll is not None and ur is not None):
        origPts = np.float32([ul, ll, ur])
        newPts = np.float32([[0, 0], [0, height - 1], [width - 1, 0]])
        warpMatrix = cv2.getAffineTransform(origPts, newPts)
        workImg = cv2.warpAffine(img, warpMatrix, (width, height))
    ch = chr(x & 0xFF)
    if ch == 'q':
        break

cv2.destroyAllWindows()
