import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../img/lenna.jpg', 0)
rows, cols = img.shape

# Fourier Transform and Shift Phase
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

# Create Gaussian Bandpass Filter
BP = np.zeros((rows, cols), np.uint8)
cv2.circle(BP, (int(rows/2), int(cols/2)), 40, 255, thickness=20, lineType=8, shift=0)
BP = cv2.GaussianBlur(BP, (7, 7), 0)

# Apply Filter
imgBP = fshift * BP

# Shift Back and Inverse Fourier Transform
f_ishift = np.fft.ifftshift(imgBP)
res = np.fft.ifft2(f_ishift)
res = np.abs(res)
imgBP = np.abs(imgBP)

plt.subplot(221), plt.imshow(img, cmap='gray')
plt.title('Input'), plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(BP, cmap='gray')
plt.title('Bandpass Filter'), plt.xticks([]), plt.yticks([])
plt.subplot(223), plt.imshow(imgBP, cmap='gray')
plt.title('Frequency Domain Output'), plt.xticks([]), plt.yticks([])
plt.subplot(224), plt.imshow(res, cmap='gray')
plt.title('Spatial Domain Output'), plt.xticks([]), plt.yticks([])
plt.show()