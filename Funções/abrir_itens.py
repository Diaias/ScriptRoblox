import cv2
import numpy as np
import mss
import time
import os

base_dir = os.path.dirname(__file__)
caminho = os.path.join(base_dir, "..", "Ibagens", "items.png")

threshold = 0.8

def detectar_tela(frame, template, threshold=0.8):

    res = cv2.matchTemplate(frame, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, _ = cv2.minMaxLoc(res)

    return max_val >= threshold

with mss.mss() as sct:

    while True:

        monitor = sct.monitors[1]

        img = np.array(sct.grab(monitor))

        cv2.imshow("debug",img)

        if cv2.waitKey(1)==27:
            break


cv2.destroyAllWindows()