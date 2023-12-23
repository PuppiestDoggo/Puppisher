import os
import subprocess
import time

from playsound import playsound
from pynput_robocorp import keyboard


def audio():
    playsound("audio.mp3")
    subprocess.run(["amixer", "-D", "pulse", "sset", "Master", "50%"])


def on_press(key):
    subprocess.Popen(["python", "supressInput.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    audio()
    subprocess.Popen(["xdg-screensaver", "lock"], stdout=subprocess.PIPE, stderr=subprocess.PIPE) # NOT WORKING IDK WHY

with keyboard.Listener(suppress=True, on_press=on_press) as listener:
    listener.join()
