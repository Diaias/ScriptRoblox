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
time.sleep(1)
subprocess.run(["py", "./Funções/prepara_orb.py"])
time.sleep(1)
subprocess.run(["py", "./Funções/clicar_orbs.py"])
time.sleep(1)
subprocess.run(["py", "./Funções/entrar_warp.py"])
time.sleep(1)
subprocess.run(["py", "./Funções/abrir_itens.py"])
time.sleep(1)
subprocess.run(["py", "./Funções/procurar_portais.py"])
time.sleep(1)
subprocess.run(["py", "./Funções/acha_portal.py"])
time.sleep(1)
subprocess.run(["py", "./Funções/setar_fraqueza.py"])
