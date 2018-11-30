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
    file_name = '{}{}.jpg'.format(SAVE_DIR, time_str)

    try:
        play_shutter_sound()
    except OSError as e:
        print('Error when executeing play_shutter_sound, error stack = ')
        print(e)
    pic.save(file_name, quality=90)
    pic.close()
    print(pic)
    print('   saved to {}'.format(file_name))

def try_clear_jam(e):
    """Clear key jam if windows + L is pressed.
    """
    stash = False
    for key in keyboard._pressed_events:
        # L, left windows or right windows
        if key == 25 or key == 91 or key == 92:
            stash = True
            break
    if stash:
        keyboard.stash_state()

if __name__ == '__main__':
    keyboard.hook(try_clear_jam)
    
    keyboard.add_hotkey('ctrl+f12', screenshot_all, args=())
    keyboard.add_hotkey('alt+f12', screenshot_all, args=())
    keyboard.add_hotkey('ctrl+f11', screenshot_all, args=())
    keyboard.add_hotkey('alt+f11', screenshot_all, args=())
    #keyboard.hook(lambda e: print(keyboard._pressed_events))


    # Block forever, like `while True`.
    keyboard.wait()
