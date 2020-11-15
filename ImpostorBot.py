import pyautogui
import time
import win32api, win32con
import keyboard

#Automate Among Us Wires

def findWire(pos: str, color: str):
    try:
        x,y = pyautogui.locateCenterOnScreen(f'{color}Wire{pos.title()}.png', confidence=0.8)
        return x,y
    except:
        pass     

#Runs the program until you press 'q'
while keyboard.is_pressed('q') == False:
    colors = ['blue', 'red', 'yellow', 'pink']
    positions = ['left', 'right']

    for color in colors:
        left = findWire('left', color)
        right = findWire('right', color)

        # if both objects are not None
        if not None in [left, right]:
            pyautogui.moveTo(left[0], left[1])
            pyautogui.drag((right[0] - left[0]), (right[1] - left[1]), duration=0.5)
