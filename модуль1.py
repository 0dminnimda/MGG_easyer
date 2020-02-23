import cv2 as cv
from mss import mss
import numpy as np

sct = mss()

whole_siz = [0, 225, 1500, 775]
siz = [350, 865, 275, 132]

while 1:
    img = np.array(sct.grab({'top': siz[1], 'left': siz[0], 'width': siz[2], 'height': siz[3]}))

    #cv.namedWindow("0", cv.WINDOW_NORMAL)
    cv.imshow("0", img)

    if cv.waitKey(1) & 0xFF == ord('2'):
        cv.destroyAllWindows()
        break