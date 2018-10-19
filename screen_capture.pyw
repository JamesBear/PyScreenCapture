import keyboard
import pyautogui
from datetime import datetime
import os
import pyaudio
import wave
import sys
import threading

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

def try_play_shutter_sound():
    try:
        play_shutter_sound()
    except OSError as e:
        print('Error when executeing play_shutter_sound, error stack = ')
        print(e)

def screenshot_all():
    print('screenshot all')
    pic = pyautogui.screenshot()
    time_str = datetime.now().strftime('%Y%m%d%H%M%S.%f')
    file_name = '{}{}.jpg'.format(SAVE_DIR, time_str)
    try_play_shutter_sound()
    pic.save(file_name, quality=90)
    pic.close()
    print(pic)
    print('   saved to {}'.format(file_name))


def restart_process():
    #like_cheese()
    print('process id:', os.getpid(), ', argv:', sys.argv)
    path = os.path.realpath(__file__)
    python_path = sys.executable.replace('python.exe', 'pythonw.exe')
    print(path)
    os.execv(python_path, ['pythonw', path])  # Run a new iteration of the current script, providing any command line args from the current iteration.

def run_watch_dog():
    import time
    time.sleep(4)
    #pyautogui.hotkey('ctrl', 'alt', 'f10')
    #try_play_shutter_sound()
    
if __name__ == '__main__':
    #try_play_shutter_sound()
    keyboard.add_hotkey('ctrl+f12', screenshot_all, args=())
    keyboard.add_hotkey('alt+f12', screenshot_all, args=())
    #keyboard.add_hotkey('ctrl+alt+f10', restart_process, args=())
    thread = threading.Thread(target=run_watch_dog)
    thread.start()

    # Block forever, like `while True`.
    keyboard.wait()
