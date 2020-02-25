import cv2 as cv
from mss import mss
import numpy as np
from finder import find
import pyscreenshot as ps

def capture(size):
    return np.array(mss().grab({'top': size[1],
                       'left': size[0],
                       'width': size[2],
                       'height': size[3]}))

def capt2(s):
    return np.array(ps.grab(bbox=[s[0], s[1], s[0]+s[2], s[1]+s[3]]))

def glob():
    return find(capt2([350, 865, 275, 132]), cv.imread('img2.png'))[1]

def reward(img):
    return find(capt2([620, 225, 290, 130]), img)[1]

def reward_h(img):
    return find(capt2([620, 225, 290, 130]), img)

if __name__ == "__main__":
    sct = mss()
    whole_siz = [0, 225, 1500, 775]
    siz = [350, 865, 275, 132]
    rev = [620, 225, 290, 130]
    link_siz = rev

    check = False
    template = cv.imread('img8.png')
    w, h = template.shape[1::-1]

    while 1:
        img = capt2(link_siz)# capture(link_siz) #capt2
        
        loc, check = reward_h(template)#find(img, template)

        if check is True:
            for pt in zip(*loc[::-1]):
                cv.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)

        #cv.namedWindow("0", cv.WINDOW_NORMAL)
        cv.imshow("0", img)

        if cv.waitKey(1) & 0xFF == ord('2'):
            cv.destroyAllWindows()
            break

    cv.imwrite("img14.png", img)