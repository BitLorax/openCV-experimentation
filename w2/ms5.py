
import cv2

for num in range(1, 8):
    img = cv2.imread("../SampleImages/Coins/coins" + str(num) + ".jpg")
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgGray, imgGray.mean() + 1.5 * imgGray.std(), 255, 0)
    contrs, hier = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    img = cv2.drawContours(img, contrs, -1, (0, 255, 0), 3)
    cv2.imshow("Contours", img)
    cv2.waitKey()
    # works best with the coins in red background
