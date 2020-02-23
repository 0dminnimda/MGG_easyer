import cv2 as cv
from mss import mss
import numpy as np

def capture(size):
    return np.array(sct.grab({'top': size[1],
                       'left': size[0],
                       'width': size[2],
                       'height': size[3]}))

sct = mss()

whole_siz = [0, 225, 1500, 775]
siz = [350, 865, 275, 132]
ico_siz = [350, 865, 275, 132]
link_siz = ico_siz

while 1:
    img = capture(link_siz)

    #cv.namedWindow("0", cv.WINDOW_NORMAL)
    cv.imshow("0", img)

    if cv.waitKey(1) & 0xFF == ord('2'):
        cv.destroyAllWindows()
        break
cv.imwrite("img.png", img)