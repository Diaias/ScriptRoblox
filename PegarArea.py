import cv2
import numpy as np
import mss

start = None
end = None
drawing = False

def mouse(event, x, y, flags, param):
    global start, end, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        start = (x, y)
        drawing = True

    elif event == cv2.EVENT_MOUSEMOVE and drawing:
        end = (x, y)

    elif event == cv2.EVENT_LBUTTONUP:
        end = (x, y)
        drawing = False


# capturar tela
with mss.mss() as sct:
    monitor = sct.monitors[1]
    screenshot = np.array(sct.grab(monitor))

img = screenshot.copy()

cv2.namedWindow("selecionar area")
cv2.setMouseCallback("selecionar area", mouse)

while True:

    temp = img.copy()

    if start and end:

        x1, y1 = start
        x2, y2 = end

        cv2.rectangle(temp, start, end, (0,255,0),2)

        width = abs(x2 - x1)
        height = abs(y2 - y1)

        text = f"X1:{x1} Y1:{y1}  X2:{x2} Y2:{y2}  W:{width} H:{height}"

        cv2.putText(
            temp,
            text,
            (20,40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0,255,0),
            2
        )

    cv2.imshow("selecionar area", temp)

    key = cv2.waitKey(1)

    if key == 13:  # ENTER
        break

cv2.destroyAllWindows()

if start and end:
    x1,y1 = start
    x2,y2 = end

    print("AREA SELECIONADA:")
    print("X1:",x1,"Y1:",y1)
    print("X2:",x2,"Y2:",y2)
    print("WIDTH:",abs(x2-x1))
    print("HEIGHT:",abs(y2-y1))