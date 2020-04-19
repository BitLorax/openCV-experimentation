
import cv2
import numpy as np


def farneback():
    cap = cv2.VideoCapture(0)

    ret, frame1 = cap.read()
    frame1 = cv2.resize(frame1, (0, 0), fx=.5, fy=.5)
    prvs = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    hsv = np.zeros_like(frame1)
    hsv[..., 1] = 255

    while True:
        ret, frame2 = cap.read()
        frame2 = cv2.resize(frame2, (0, 0), fx=.5, fy=.5)  # small enough to run in real-time
        next = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

        flow = cv2.calcOpticalFlowFarneback(prvs, next, None, 0.5, 3, 15, 3, 5, 1.2, 0)

        mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])
        hsv[..., 0] = ang * 180 / np.pi / 2
        hsv[..., 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
        bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

        cv2.imshow('frame2', bgr)
        k = chr(cv2.waitKey(30) & 0xff)
        if k == 'q':
            break
        elif k == 's':
            cv2.imwrite('opticalfb.png', frame2)
            cv2.imwrite('opticalhsv.png', bgr)
        prvs = next

    cap.release()
    cv2.destroyAllWindows()


def kanade():
    cap = cv2.VideoCapture(0)

    # Create some random colors
    color = np.random.randint(0, 255, (100, 3))

    # Wait until user is ready to start tracking, user hits space to go on
    while True:
        ret, old_frame = cap.read()

        cv2.imshow("Frame", old_frame)
        c = chr(cv2.waitKey(10) & 0xFF)
        if c == ' ':
            break

    # Grap features on most recent frame using Shi-Tomasi
    old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
    p0 = cv2.goodFeaturesToTrack(old_gray,
                                 mask=None,
                                 maxCorners=100,
                                 qualityLevel=0.3,
                                 minDistance=7,
                                 blockSize=3)
    # Create a mask image for drawing purposes
    mask = np.zeros(old_frame.shape, old_frame.dtype)

    # Loop over video while tracking
    while True:
        ret, frame = cap.read()
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        tp0 = cv2.goodFeaturesToTrack(old_gray,
                                      mask=None,
                                      maxCorners=100,
                                      qualityLevel=0.3,
                                      minDistance=7,
                                      blockSize=3)

        # add new corners, keep maximum 100
        p0 = np.concatenate((p0, tp0), axis=0)
        if (p0.shape[0] > 100):
            p0 = p0[0:100, :, :]

        # calculate optical flow
        p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None,
                                               winSize=(15, 15),
                                               maxLevel=2,
                                               criteria=(cv2.TERM_CRITERIA_EPS
                                                         | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

        # Select good points
        good_new = p1[st == 1]
        good_old = p0[st == 1]

        # draw the tracks
        for i, (new, old) in enumerate(zip(good_new, good_old)):
            a, b = new.ravel()
            c, d = old.ravel()
            mask = cv2.line(mask, (a, b), (c, d), color[i].tolist(), 2)
            frame = cv2.circle(frame, (a, b), 5, color[i].tolist(), -1)
        img = cv2.add(frame, mask)

        cv2.imshow('Frame', img)
        k = chr(cv2.waitKey(30) & 0xff)
        if k == 'q':
            break

        # Now update the previous frame and previous points
        old_gray = frame_gray.copy()
        p0 = good_new.reshape(-1, 1, 2)

    cv2.destroyAllWindows()
    cap.release()


farneback()
