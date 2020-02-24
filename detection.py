import cv2 as cv
from mss import mss
import numpy as np
from finder import find

sct = mss()

def capture(size):
    return np.array(sct.grab({'top': size[1],
                       'left': size[0],
                       'width': size[2],
                       'height': size[3]}))

def glob():
    return find(capture([350, 865, 275, 132]), cv.imread('img2.png'))[1]

if __name__ == "__main__":
    whole_siz = [0, 225, 1500, 775]
    siz = [350, 865, 275, 132]
    link_siz = siz

    check = False
    template = cv.imread('img2.png')
    w, h = template.shape[1::-1]

    while 1:
        img = capture(link_siz)

        loc, check = find(img, template)

        if check is True:
            for pt in zip(*loc[::-1]):
                cv.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)

        #cv.namedWindow("0", cv.WINDOW_NORMAL)
        cv.imshow("0", img)

        if cv.waitKey(1) & 0xFF == ord('2'):
            cv.destroyAllWindows()
            break

    #cv.imwrite("img12.png", img)