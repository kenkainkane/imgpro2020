import cv2
import numpy as np

def saltAndPepper(img, occurRate):
    row, col = img.shape
    s_vs_p = 0.5    # salt - pepper ratio
    out = img
    salt = np.ceil(occurRate * img.size * s_vs_p)
    coords = [np.random.randint(0, i-1, int(salt))
                for i in img.shape]
    out[coords] = 255
    pepper = np.ceil(occurRate * img.size * (1. - s_vs_p))
    coords = [np.random.randint(0, i-1, int(pepper))
                for i in img.shape]
    out[coords] = 0
    return out

def gaussianNoise(img):
    row, col = img.shape
    mean = 0
    var = 0.1
    sigma = var**0.5
    gauss = np.random.normal(mean, sigma,(row, col))
    gauss = gauss.reshape(row, col)
    out = img + gauss
    out = out.astype(np.uint8)
    return out
    
img = cv2.imread('../img/lenna.jpg', 0)
img_sp = saltAndPepper(img.copy(), 0.1)
img_gs = gaussianNoise(img.copy())

cv2.imshow("Original", img)
cv2.imshow("Salt & Pepper", img_sp)
cv2.imshow("Gaussian", img_gs)

cv2.waitKey(0)
cv2.destroyAllWindows()