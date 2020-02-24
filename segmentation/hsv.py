import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../img/m&m.jpg')
b, g, r = cv2.split(img)

# Convert to HSV Color Space
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
upper = np.array([166, 255, 255])
lower = np.array([76, 61, 0])
mask = cv2.inRange(hsv, lower, upper)

row, col, ch = img.shape
res = np.zeros((row, col, 3), np.uint8)
res_b, res_g, res_r = cv2.split(res)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

for i in range (0, row):
    for j in range (0, col):
        if mask[i][j] == 0:
            res_b[i][j] = gray[i][j]
            res_g[i][j] = gray[i][j]
            res_r[i][j] = gray[i][j]
        else:
            res_b[i][j] = b[i][j]
            res_g[i][j] = g[i][j]
            res_r[i][j] = r[i][j]
res = cv2.merge((res_b, res_g, res_r))
cv2.imshow('result', res)
cv2.waitKey(0)
cv2.destroyAllWindows()