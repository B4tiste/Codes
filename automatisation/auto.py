"""
    automatisation python
"""

import os
import time
from pynput.keyboard import Key, Controller

login = "aze"
password = "qsd"

# Open microsoft Word
# os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE")

# Open a chrome browser and go to the url
url = 'http://127.0.0.1:5500/automatisation/index.html'
os.startfile(url)

time.sleep(2)


keyboard = Controller()


def press(key):
    keyboard.press(key)


def release(key):
    keyboard.release(key)

press(Key.tab)
release(Key.tab)

for lettre in login :
    press(lettre)
    release(lettre)

press(Key.tab)
release(Key.tab)

for lettre in password:
    press(lettre)
    release(lettre)

press(Key.tab)
release(Key.tab)

press(Key.enter)
release(Key.enter)

press(Key.tab)
release(Key.tab)

press(Key.enter)
release(Key.enter)

press(Key.ctrl_l)
press("l")
release(Key.ctrl_l)
release("l")