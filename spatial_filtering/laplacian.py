import cv2
import numpy as np

img = cv2.imread('../img/lenna.jpg', 0)

# create laplacian filter
laplacian = np.array((
    [1, 1, 1],
    [1, -4, 1],
    [1, 1, 1]), dtype="int")

lap = cv2.filter2D(img, -1, laplacian)

# output = img + c * laplacian (Using negative c if center of filter is negative. And vice versa.)
cv2.imshow('original', img)
cv2.imshow('laplacian', img-lap)

cv2.waitKey(0)
cv2.destroyAllWindows()