
import cv2
import os


def partA(file):
    img = cv2.imread("../SampleImages/Coins/" + file)
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # sobelH = cv2.Sobel(imgGray, cv2.CV_32F, 1, 0)
    # sobelV = cv2.Sobel(imgGray, cv2.CV_32F, 0, 1)
    # sobel = cv2.addWeighted(sobelH, 0.5, sobelV, 0.5, 0)
    # sobelImg = cv2.convertScaleAbs(sobel)
    # cv2.imshow("Sobel", sobelImg)

    canny = cv2.Canny(imgGray, 100, 150)
    cv2.imshow("Canny", canny)

    cv2.waitKey()


def partB(file):
    img = cv2.imread("../SampleImages/CardsAndSigns/" + file)
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    canny = cv2.Canny(imgGray, 50, 100)
    cv2.imshow("Canny", canny)

    cv2.waitKey()


def partC(file):
    img = cv2.imread("../SampleImages/PuzzlesAndGames/" + file)
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    canny = cv2.Canny(imgGray, 50, 100)  # same config as partB works well too
    cv2.imshow("Canny", canny)

    cv2.waitKey()


# for file in os.listdir("../SampleImages/Coins"):
#     partA(file)
# for file in os.listdir("../SampleImages/CardsAndSigns"):
#     partB(file)
for file in os.listdir("../SampleImages/PuzzlesAndGames"):
    partC(file)
