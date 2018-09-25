import keyboard
import pyautogui
from datetime import datetime
import os

SAVE_DIR = 'C:\\screenshots\\'

if not os.path.isdir(SAVE_DIR):
    os.mkdir(SAVE_DIR)

def screenshot_all():
    print('screenshot all')
    pic = pyautogui.screenshot()
    time_str = datetime.now().strftime('%Y%m%d%H%M%S.%f')
    file_name = '{}{}.png'.format(SAVE_DIR, time_str)

    pic.save(file_name)
    print('   saved to {}'.format(file_name))

keyboard.add_hotkey('ctrl+f12', screenshot_all, args=())

# Block forever, like `while True`.
keyboard.wait()
