import cv2
import numpy as np
import pyautogui
import mss
import os
import time

base_dir = os.path.dirname(__file__)
pasta = os.path.join(base_dir, "..", "Ibagens", "Vantagem")

# lista de templates
templates = {
    "Amarelo": cv2.imread(os.path.join(pasta, "Amarelo.png")),
    "Azul": cv2.imread(os.path.join(pasta, "Azul.png")),
    "Roxo": cv2.imread(os.path.join(pasta, "Roxo.png")),
    "Verde": cv2.imread(os.path.join(pasta, "Verde.png")),
    "Vermelho": cv2.imread(os.path.join(pasta, "Vermelho.png")),
}

threshold = 0.8

scales = np.linspace(0.2, 1.3, 10)

with mss.MSS() as sct:

    time.sleep(2)
    
    mouse_x, mouse_y = pyautogui.position()
    monitor = {
        "left": mouse_x,
        "top": mouse_y,
        "width": 500,
        "height": 800
    }

    while True:
        img = np.array(sct.grab(monitor))
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

        best_val = 0
        best_name = None
        best_loc = None
        best_size = None

        for name, template in templates.items():

            if template is None:
                continue
            for scale in scales:
                resized = cv2.resize(template, None, fx=scale, fy=scale)

                # evita erro se ficar maior que a tela
                if resized.shape[0] > img.shape[0] or resized.shape[1] > img.shape[1]:
                    continue

                res = cv2.matchTemplate(img, resized, cv2.TM_CCOEFF_NORMED)
                _, max_val, _, max_loc = cv2.minMaxLoc(res)

                if max_val > best_val:
                    best_val = max_val
                    best_name = name
                    best_loc = max_loc
                    best_size = resized.shape[:2]

        if best_val >= threshold:
            print(f"Encontrou: {best_name} ({best_val:.2f})")

            break
        else:
            print("Nada encontrado")