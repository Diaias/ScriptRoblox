import cv2
import numpy as np
import pyautogui
import mss
import os
import time
import keyboard
import pydirectinput

base_dir = os.path.dirname(__file__)

caminho = os.path.join(base_dir, "..", "Ibagens", "ir_orbs_ALT.png")
template = cv2.imread(caminho, cv2.IMREAD_COLOR)
template = cv2.cvtColor(template, cv2.COLOR_BGR2RGB)

caminho_inner = os.path.join(base_dir, "..", "Ibagens", "botao_play_ALT.png")
template_inner = cv2.imread(caminho_inner, cv2.IMREAD_COLOR)
template_inner = cv2.cvtColor(template_inner, cv2.COLOR_BGR2RGB)

threshold = 0.7
threshold_inner = 0.7

scales = np.linspace(0.1, 1, 10)

with mss.MSS() as sct:
    monitor = sct.monitors[1]

    while True:
        img = np.array(sct.grab(monitor))
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2RGB)

        best_val = 0
        best_loc = None
        best_size = None

        for scale in scales:
            resized = cv2.resize(template, None, fx=scale, fy=scale)

            if resized.shape[0] > img.shape[0] or resized.shape[1] > img.shape[1]:
                continue

            res = cv2.matchTemplate(img, resized, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, max_loc = cv2.minMaxLoc(res)

            if max_val > best_val:
                best_val = max_val
                best_loc = max_loc
                best_size = resized.shape[:2]

        if best_val >= threshold:
            print("ACHOU GRANDE!", best_val)

            h, w = best_size
            x, y = best_loc

            recorte = img[y:y+h, x:x+w]

            res2 = cv2.matchTemplate(recorte, template_inner, cv2.TM_CCOEFF_NORMED)
            _, max_val2, _, max_loc2 = cv2.minMaxLoc(res2)

            if max_val2 >= threshold_inner:
                print("ACHOU DENTRO!", max_val2)

                ih, iw = template_inner.shape[:2]

                inner_x = x + max_loc2[0] + iw // 2
                inner_y = y + max_loc2[1] + ih // 2

                pydirectinput.moveTo(inner_x - 10, inner_y)
                pydirectinput.moveTo(inner_x, inner_y)
                time.sleep(0.2)
                pydirectinput.mouseDown(button='left')
                time.sleep(0.1)
                pydirectinput.mouseUp(button='left')

                break
            else:
                print(f"Inner não achou: {max_val2:.2f}")

        else:
            print(f"Melhor match: {best_val:.2f}")