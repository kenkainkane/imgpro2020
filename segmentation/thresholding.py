import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../img/lenna.jpg',0)
ret,thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('result', thresh)
cv2.waitKey()
cv2.destroyAllWindows()