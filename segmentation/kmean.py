import cv2
import numpy as np
import matplotlib.pyplot as plt

# read the image and convert to rgb
image = cv2.imread('../img/m&m.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# reshape the image to a 2D array of pixels and 3 color values (RGB)
pixel_values = image.reshape((-1, 3))
pixel_values = np.float32(pixel_values)

# define stopping criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
k = 5
_, labels, (centers) = cv2.kmeans(pixel_values, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
centers = np.uint8(centers)
labels = labels.flatten()

# convert all pixels to the color of the centroids
segmented_image = centers[labels.flatten()]
segmented_image = segmented_image.reshape(image.shape)
cv2.imshow('result', segmented_image)
cv2.waitKey()
cv2.destroyAllWindows()