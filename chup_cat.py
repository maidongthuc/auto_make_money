import subprocess
from time import sleep
import os
import cv2
import requests
import base64
import pandas as pd
adb_path = 'E:/SELENIUM/CWIN/REG_2/ADB/adb.exe'
device = 'emulator-5554'

def capture_screenshot(device, filename):
    screenshot_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
    command = f'{adb_path} -s {device} exec-out screencap -p > {screenshot_path}'
    subprocess.call(command, shell=True)
    print(f'Screenshot saved to {screenshot_path}')

def crop_image(input_image_path = 'E:\\SELENIUM\\CWIN\\REG_2\\home_2.png', output_image_path = 'E:\\SELENIUM\\CWIN\\REG_2\\bo_nho.png'):
    image = cv2.imread(input_image_path)
    x1, y1, x2, y2 = 0, 800, 300, 1000
    cropped_image = image[y1:y2, x1:x2]
    cv2.imwrite(output_image_path, cropped_image)
    print(f'Image cropped and saved to {output_image_path}')
capture_screenshot(device, 'home_2.png')