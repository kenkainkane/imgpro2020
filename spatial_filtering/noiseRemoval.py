import cv2
import numpy as np

img_sp = cv2.imread('../img/saltAndPepper.jpg')
img_gs = cv2.imread('../img/gaussian.jpg')

# smoothing image using average filter
avg_blur_sp = cv2.blur(img_sp, (7, 7))
avg_blur_gs = cv2.blur(img_gs, (7, 7))

# smoothing image using median filter
med_blur_sp = cv2.medianBlur(img_sp, 5)
med_blur_gs = cv2.medianBlur(img_gs, 5)

cv2.imshow('average salt&pepper', avg_blur_sp)
cv2.imshow('average gaussian', avg_blur_gs)
cv2.imshow('median salt&pepper', med_blur_sp)
cv2.imshow('median gaussian', med_blur_gs)

cv2.waitKey()
cv2.destroyAllWindows()