import cv2
import numpy as np

img = cv2.imread('../img/lenna.jpg', 0)

blur = cv2.blur(img, (5, 5))
diff = img - blur # find edges
sharpen = img + diff

cv2.imshow('Original', img)
cv2.imshow('Edges', diff)
cv2.imshow('Sharpen', sharpen)

cv2.waitKey(0)
cv2.destroyAllWindows()