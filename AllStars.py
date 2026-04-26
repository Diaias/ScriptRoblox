import subprocess
import time
import os
import cv2
import numpy as np
import mss
import keyboard
import pyautogui

time.sleep(3)

subprocess.run(["py", "./Funções/entrar_warp.py"])
time.sleep(0.2)
subprocess.run(["py", "./Funções/prepara_orb.py"])
time.sleep(0.2)
subprocess.run(["py", "./Funções/clicar_orbs.py"])
time.sleep(0.2)
subprocess.run(["py", "./Funções/entrar_warp.py"])
time.sleep(0.2)
subprocess.run(["py", "./Funções/abrir_itens.py"])
time.sleep(0.2)
subprocess.run(["py", "./Funções/procurar_portais.py"])
time.sleep(0.2)
subprocess.run(["py", "./Funções/acha_portal.py"])
time.sleep(0.2)
resultado = subprocess.run(
    ["py", "./Funções/setar_fraqueza.py"],
    capture_output=True,
    text=True
)
cor_da_fraqueza = resultado.stdout.strip()
print(f"Cor da fraqueza: {cor_da_fraqueza}")
