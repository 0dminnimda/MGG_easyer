import cv2 as cv
import numpy as np

def find(img, template, threshold=0.99):
    img_rgb = img
    img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)

    template = cv.cvtColor(template, cv.COLOR_BGR2GRAY)
    w, h = template.shape[::-1]

    res = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)
    threshold = 0.99
    loc = np.where(res >= threshold)

    return img_rgb, loc, w, h

img = cv.imread('img.png')
template = cv.imread('img2.png')
img_rgb, loc, w, h = find(img, template)
print(loc[0].shape, loc[0].shape)

while 1:
    for pt in zip(*loc[::-1]):
        cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)

    if cv.waitKey(1) & 0xFF == ord('2'):
        cv.destroyAllWindows()
        break

    cv.imshow('Detected', img_rgb)