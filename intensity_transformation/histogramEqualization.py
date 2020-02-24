import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load image and convert to grayscale
im = cv2.imread('../img/lenna.jpg', 0)

# Equalization
eq = cv2.equalizeHist(im)

# Plotting Histograms
grayHis = cv2.calcHist([im], [0], None, [256], [0, 256])
plt.subplot(211)
plt.plot(grayHis)

eqHis = cv2.calcHist([eq], [0], None, [256], [0, 256])
plt.subplot(212)
plt.plot(eqHis)

cv2.imshow('original', im)
cv2.imshow('equlized', eq)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()