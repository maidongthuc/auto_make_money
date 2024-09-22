import subprocess
from time import sleep
import os
import cv2
import requests
import base64
import pandas as pd
import numpy as np

url = "https://mproxy.vn/capi/aimwlugm_5WhOej62Q9_JN57ct4vFhCBP6bTTcjGUKw/key/BIU2qMXAqgMOEzLM/resetIp"
user = 'chechanh2003'
passworld = 'BIU2qMXAqgMOEzLM'

data = pd.read_csv('E:/SELENIUM/CWIN/REG_2/data3.csv', header=None).values

adb_path = 'E:/SELENIUM/CWIN/REG_2/ADB/adb.exe'
device = 'emulator-5554'
image_path = 'E:/SELENIUM/CWIN/REG_2/'

def tap(device, x, y):
    command = f'{adb_path} -s {device} shell input tap {x} {y}'
    subprocess.call(command, shell=True)
def swipe(device, x1, y1, x2, y2, duration=1000):
    command = f'{adb_path} -s {device} shell input swipe {x1} {y1} {x2} {y2} {duration}'
    subprocess.call(command, shell=True)
def input_text(device, text):
    formatted_text = text.replace(' ', '%s')
    command = f'{adb_path} -s {device} shell input text "{formatted_text}"'
    subprocess.call(command, shell=True)
def press_enter(device):
    command = f'{adb_path} -s {device} shell input keyevent 66'
    subprocess.call(command, shell=True)
def capture_screenshot(device, filename = 'temp.png'):
    screenshot_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
    command = f'{adb_path} -s {device} exec-out screencap -p > {screenshot_path}'
    subprocess.call(command, shell=True)
    # print(f'Screenshot saved to {screenshot_path}')
def crop_image(input_image_path = 'E:\\SELENIUM\\CWIN\\REG_2\\temp.png', output_image_path = 'E:\\SELENIUM\\CWIN\\REG_2\\cropped_image.png'):
    image = cv2.imread(input_image_path)
    x1, y1, x2, y2 = 507, 1080, 593, 1120
    cropped_image = image[y1:y2, x1:x2]
    cv2.imwrite(output_image_path, cropped_image)
    # print(f'Image cropped and saved to {output_image_path}')
def solve_captcha(api_key, image_data, captcha_type):
    api_url = "https://anticaptcha.top/api/captcha"
    payload = {
        "apikey": api_key,
        "img": image_data,
        "type": captcha_type
    }
    headers = {
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(api_url, json=payload, headers=headers)
        if response.status_code == 200:
            result = response.json()
            return result
        else:
            print(f"Yêu cầu không thành công. Mã trạng thái: {response.status_code}")
            return None
    except Exception as e:
        print(f"Lỗi khi gửi yêu cầu đến API: {e}")
        return None

def giai_cap_cha():
    with open('E:\\SELENIUM\\CWIN\\REG_2\\cropped_image.png', 'rb') as image_file:
        # Đọc dữ liệu nhị phân của hình ảnh
        binary_data = image_file.read()

        # Mã hóa dữ liệu nhị phân thành chuỗi base64
        base64_data = base64.b64encode(binary_data).decode('utf-8')
    api_key = "edc99c4c32c281614558673fa2139626"
    image_url = base64_data  # Đặt URL của ảnh captcha ở đây
    captcha_type = 0  # Đặt loại captcha bạn muốn giải
    result = solve_captcha(api_key, image_url, captcha_type)
    capcha = result['captcha']
    for j in range(4):
        if(capcha[j] == 'o'):
            capcha = capcha.replace('o', '0')
    # print(capcha)
    return capcha

def index_object(img_large_path, img_small_path):
    img_large = cv2.imread(f'{image_path}{img_large_path}')
    img_small = cv2.imread(f'{image_path}{img_small_path}')
    img_large_gray = cv2.cvtColor(img_large, cv2.COLOR_BGR2GRAY)
    img_small_gray = cv2.cvtColor(img_small, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(img_large_gray, img_small_gray, cv2.TM_CCOEFF_NORMED)
    threshold = 0.9
    loc = np.where(result >= threshold)
    test_data = list(zip(*loc[::-1]))
    return test_data
def wait_done(path):
    while(1):
        capture_screenshot(device)
        if(len(index_object('temp.png',path))>0):
            tap(device, index_object('temp.png',path)[0][0]+10,index_object('temp.png',path)[0][1]+10)
            break
        continue
for i in range(1,30):
    wait_done('system_apps.png')
    wait_done('cai_dat.png')
    wait_done('bo_nho.png')
    wait_done('ung_dung_khac.png')
    sleep(1)
    wait_done('duckduck_1.png')
    wait_done('xoa_bo_nho.png')
    wait_done('ok_1.png')
    wait_done('vuong.png')
    wait_done('xoa_tat_ca.png')
    wait_done('duckduck_2.png')
    wait_done('let_do_it.png')
    wait_done('choose_your_browser.png')
    sleep(2)
    input_text(device, 'https://m.cwin7700.com/')
    press_enter(device)
    sleep(1)
    input_text(device, user)
    tap(device, 170, 697) # nhấn pass
    input_text(device, passworld)
    tap(device, 493, 800) # nhấn login
    wait_done('got_it.png')
    sleep(1)
    tap(device, 561, 91)
    sleep(1)
    tap(device, 159, 1245)
    capture_screenshot(device)
    if(len(index_object('temp.png','khong_kha_dung.png'))>0):
        tap(device, 561, 91)
        sleep(1)
        tap(device, 126, 1163)
        sleep(3)
        tap(device, 694, 303)
        sleep(1)
        tap(device, 628, 92)
        sleep(1)
        continue
    while(1):
        capture_screenshot(device)
        if(len(index_object('temp.png','tin_tuc_moi_nhat.png'))>0):
            tap(device, 620, 787)
            break
    wait_done('toi_biet_roi.png')
    wait_done('dang_ky.png')
    while(1):
        capture_screenshot(device)
        if(len(index_object('temp.png','dieu_kien_dang_ky.png'))>0):
            break
    sleep(3)
    tap(device, 137, 504)
    input_text(device, data[i][0])
    tap(device, 135, 650)
    input_text(device, data[i][1])
    tap(device, 135, 775)
    input_text(device, data[i][1])
    tap(device, 135, 895)
    input_text(device, data[i][2])
    while(1):
        tap(device, 135, 1076)
        sleep(4)
        capture_screenshot(device)
        crop_image()
        input_text(device, giai_cap_cha())
        tap(device, 135, 1250)
        sleep(3)
        capture_screenshot(device)
        if(len(index_object('temp.png','xac_nhan.png'))>0):
            print(index_object('temp.png','xac_nhan.png'))
            tap(device, 135, 1076)
            continue
        break 
    if(len(index_object('temp.png','bat_dau_tro_choi.png'))>0):
        tap(device, index_object('temp.png','bat_dau_tro_choi.png')[0][0]+10,index_object('temp.png','bat_dau_tro_choi.png')[0][1]+10)
        print(f'{i+1}  {data[i]}  DONE')
        wait_done('not_now.png')
        # print('done')
    else:
        print(f'{i+1}  {data[i]}  X')
        # print('NO done')
    sleep(1)
    tap(device, 561, 91)
    sleep(1)
    tap(device, 126, 1163)
    sleep(3)
    tap(device, 561, 91)
    sleep(1)
    tap(device, 126, 1163)
    sleep(3)
    tap(device, 694, 303)
    sleep(1)
    tap(device, 628, 92)
    sleep(1)
    response = requests.get(url)
    if response.status_code == 200:
        # Parse the JSON response
        json_data = response.json()
        # Print the JSON response
        print(json_data)
        #print(json_data)
    else:
        # If the request failed, print the status code
        print(f"Failed to get a valid response. Status code: {response.status_code}")