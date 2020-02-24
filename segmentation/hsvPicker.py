import cv2
import sys
import numpy as np

def nothing(x):
    pass

lowH = 0
lowS = 0
lowV = 0
highH = 179
highS = 255
highV = 255

cv2.namedWindow('HSV Scale')

cv2.createTrackbar('lowH',  'HSV Scale', lowH , 179, nothing)
cv2.createTrackbar('highH', 'HSV Scale', highH, 179, nothing)

cv2.createTrackbar('lowS' , 'HSV Scale', lowS , 255, nothing)
cv2.createTrackbar('highS', 'HSV Scale', highS, 255, nothing)

cv2.createTrackbar('lowV' , 'HSV Scale', lowV , 255, nothing)
cv2.createTrackbar('highV', 'HSV Scale', highV, 255, nothing)


while True:
    frame = cv2.imread(str(sys.argv[1])) 

    lowH = cv2.getTrackbarPos('lowH', 'HSV Scale')
    lowS = cv2.getTrackbarPos('lowS', 'HSV Scale')
    lowV = cv2.getTrackbarPos('lowV', 'HSV Scale')

    highH = cv2.getTrackbarPos('highH', 'HSV Scale')
    highS = cv2.getTrackbarPos('highS', 'HSV Scale')
    highV = cv2.getTrackbarPos('highV', 'HSV Scale')

    lower = np.array([lowH, lowS, lowV])
    upper = np.array([highH, highS, highV])

    #frame = cv2.resize(frame, None, fx=0.5, fy=0.5)
    blurred = cv2.GaussianBlur(frame, (5, 5), 0)

    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, lower, upper)
    frame = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('Original', cv2.resize(frame,None,fx=0.5,fy=0.5))
    cv2.imshow('Frame:', cv2.resize(mask,None,fx=0.5,fy=0.5))
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cv2.destroyAllWindows()
