
import cv2
import os


def clean(path):  # try using inRange
    img = cv2.imread("../SampleImages/" + path)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.GaussianBlur(img, (11, 11), 0)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
    for i in range(0, 3):
        img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    _, img = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
    for i in range(0, 3):
        img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    img = cv2.GaussianBlur(img, (11, 11), 0)

    cv2.imshow("Img", img)
    cv2.waitKey()


for file in os.listdir("../SampleImages/PuzzlesAndGames"):
    clean("PuzzlesAndGames/" + file)
    # not effective on sudoku as the closing eliminates most of the grid
    # comment out the two for loops for sudoku
