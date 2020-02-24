import cv2
import numpy as np

# Load image and convert to grayscale
img = cv2.imread('../img/lenna.jpg', 0)

# Adjust gamma = 0.5
lowGammaImg = np.power(img/255, 0.5)

# Adjust gamme = 1.5
highGammaImg = np.power(img/255, 1.5)

cv2.imshow('original', img)
cv2.imshow('lowGammaImg', lowGammaImg)
cv2.imshow('highGammaImg', highGammaImg)

cv2.waitKey(0)
cv2.destroyAllWindows()
