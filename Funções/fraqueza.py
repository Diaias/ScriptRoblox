import cv2
import numpy as np
import mss
import os
import time
import keyboard
import pyautogui

base_dir = os.path.dirname(__file__)
caminho = os.path.join(base_dir, "..", "Ibagens", "icone_portal.png")

template = cv2.imread(caminho, cv2.IMREAD_COLOR)
template = cv2.cvtColor(template, cv2.COLOR_BGR2RGB)

threshold = 0.7

scales = np.linspace(0.7, 1.3, 10)

with mss.mss() as sct:
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
            print("ACHOU!", best_val)

            h, w = best_size

            center_x = best_loc[0] + w // 2
            center_y = best_loc[1] + h // 2

            pyautogui.moveTo(center_x + 10, center_y)
            pyautogui.moveTo(center_x, center_y)


            break
        else:
            print(f"Melhor match: {best_val:.2f}")