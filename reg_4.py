import subprocess
from time import sleep
import os
import cv2
import requests
import numpy as np
import pandas as pd

adb_path = 'E:/SELENIUM/CWIN/REG_2/ADB/adb.exe'
device = 'emulator-5554'
image_path = 'E:/SELENIUM/CWIN/REG_2/'

def index_object(img_large_path, img_small_path):
    img_large = cv2.imread(f'{image_path}{img_large_path}')
    img_small = cv2.imread(f'{image_path}{img_small_path}')
    img_large_gray = cv2.cvtColor(img_large, cv2.COLOR_BGR2GRAY)
    img_small_gray = cv2.cvtColor(img_small, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(img_large_gray, img_small_gray, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(result >= threshold)
    test_data = list(zip(*loc[::-1]))
    return test_data
def tap(device, x, y):
    command = f'{adb_path} -s {device} shell input tap {x} {y}'
    subprocess.call(command, shell=True)
# sleep(1)
# tap(device, index_object('home_2.png','user_proxy.png')[0][0]+10, index_object('home_2.png','user_proxy.png')[0][1]+10) # nhấn duckduckgo

# sleep(3)
print(index_object('blum7.png','object1.png'))
