import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load image and convert to grayscale
img = cv2.imread('../img/lenna.jpg', 0)
rows, cols = img.shape

# Fourier Transform
dft = cv2.dft(np.float32(img), flags = cv2.DFT_REAL_OUTPUT)
dft_shift = np.fft.fftshift(dft)

# Create Lowpass Filter
r = 40
LP = np.zeros((rows, cols),np.uint8)
for i in range (1, rows):
    for j in range (1, cols):
        if ((i - rows/2) ** 2 + (j - cols/2) ** 2) < r ** 2:
            LP[i, j] =  1

# Apply Filter
res = dft_shift * LP
res_shift = np.fft.ifftshift(res)

# Inverse Fourier Transform
output = cv2.idft(res_shift)
output = np.abs(output)

# Plot
plt.subplot(121), plt.imshow(img, cmap = 'gray')
plt.title('Before'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(output, cmap = 'gray')
plt.title('After'), plt.xticks([]), plt.yticks([])
plt.show()