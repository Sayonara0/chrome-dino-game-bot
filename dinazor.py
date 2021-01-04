from PIL import ImageGrab, ImageOps
import pyautogui
from numpy import *
import keyboard

while True:
    x,y,a,b = 414,560,252,121
    box = (x,y,x+a,y+b)
    image = ImageGrab.grab(box)
    gray = ImageOps.grayscale(image)
    a = array(gray.getcolors())
    value = a.sum()
    print(value)
    if value == 31079 or value == 30830:
        print("i will jump")
        pyautogui.press('space')

