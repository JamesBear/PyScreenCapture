import keyboard
import pyautogui
from datetime import datetime
import os
import pyaudio
import wave
import sys

SAVE_DIR = 'C:\\screenshots\\'
WAV_FILE = 'camera4.wav'
wf = None

if not os.path.isdir(SAVE_DIR):
    os.mkdir(SAVE_DIR)

def play_shutter_sound():
    CHUNK = 1024

    global wf
    if wf == None:
        wf = wave.open(WAV_FILE, 'rb')
    wf.setpos(0)
    p = pyaudio.PyAudio()


    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    data = wf.readframes(CHUNK)

    while data != '' and data != b'':
        stream.write(data)
        data = wf.readframes(CHUNK)

    stream.stop_stream()
    stream.close()

    p.terminate()

def screenshot_all():
    print('screenshot all')
    pic = pyautogui.screenshot()
    time_str = datetime.now().strftime('%Y%m%d%H%M%S.%f')
    file_name = '{}{}.png'.format(SAVE_DIR, time_str)

    pic.save(file_name)
    print('   saved to {}'.format(file_name))
    play_shutter_sound()

if __name__ == '__main__':
    keyboard.add_hotkey('ctrl+f12', screenshot_all, args=())

    # Block forever, like `while True`.
    keyboard.wait()
