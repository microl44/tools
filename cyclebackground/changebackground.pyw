import struct
import ctypes
from time import sleep
import os
import sys

path = os.getcwd() + "\\pyw"

print(path)

files = os.listdir(path)

SPI_SETDESKWALLPAPER = 20

def is_64bit_windows():
    """Check if 64 bit Windows OS"""
    return struct.calcsize('P') * 8 == 64

def changeBG(bg):
    """Change background depending on bit size"""
    if is_64bit_windows():
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, bg, 3)
    else:
        ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, bg, 3)


while True:
    for file in files:
        if ".png" in file:
            changeBG(os.path.join(path, file))
            sleep(1)