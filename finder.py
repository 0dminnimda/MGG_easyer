import cv2 as cv
import numpy as np

def find(img_rgb, template, threshold=0.99):
    img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)

    template = cv.cvtColor(template, cv.COLOR_BGR2GRAY)

    res = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)

    return img_rgb, loc

img = cv.imread('img.png')
template = cv.imread('img4.png')
w, h = template.shape[1::-1]
img_rgb, loc = find(img, template)
print(loc[0].shape, loc[0].shape)

while 1:
    for pt in zip(*loc[::-1]):
        cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)

    if cv.waitKey(1) & 0xFF == ord('2'):
        cv.destroyAllWindows()
        break

    cv.imshow('Detected', img_rgb)