from PIL import ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics
import datetime

def screen():
    width = GetSystemMetrics(0)
    height = GetSystemMetrics(1)
    
    time_stamp = datetime.datetime.now().strftime('%d-%m-%Y_%H-%M-%S')
    file_name = (f"{time_stamp}.mp4")

    venv = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    captured_video = cv2.VideoWriter(file_name, venv, 20.0, (width, height))

    while True:
        img = ImageGrab.grab(bbox=(0, 0, width, height))
        img_np = np.array(img)
        img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)

        cv2.imshow('Screen Recording', img_final)
        captured_video.write(img_final)
        if cv2.waitKey(1) == ord('q'):
            break