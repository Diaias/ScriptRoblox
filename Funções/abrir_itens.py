import cv2
import numpy as np
import mss
import os
import pyautogui

# caminho correto
base_dir = os.path.dirname(__file__)
caminho = os.path.join(base_dir, "..", "Ibagens", "items.png")  # corrigido

# carregar template
template = cv2.imread(caminho, cv2.IMREAD_COLOR)

threshold = 0.8

with mss.mss() as sct:
    monitor = sct.monitors[1]

    while True:
        img = np.array(sct.grab(monitor))
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

        res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(res)

        if max_val >= threshold:
            print("Imagem encontrada!", max_val)

            # pega tamanho do template
            h, w = template.shape[:2]

            # calcula centro
            center_x = max_loc[0] + w // 2
            center_y = max_loc[1] + h // 2

            print("Centro:", center_x, center_y)

            # clica
            pyautogui.click(center_x, center_y)

            break
        else:
            print("Não encontrou")

cv2.destroyAllWindows()