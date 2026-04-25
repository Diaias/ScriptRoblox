import cv2
import numpy as np
import os
import mss

with mss.mss() as sct:

    monitor = {"top": 100, "left": 100, "width": 800, "height": 600}

    while True:

        img = np.array(sct.grab(monitor))[:,:,:3]

        img = cv2.GaussianBlur(img,(3,3),0)

        debug = img.copy()

        cv2.imshow("debug triangulo",debug)

        if cv2.waitKey(1)==27:
            break


cv2.destroyAllWindows()