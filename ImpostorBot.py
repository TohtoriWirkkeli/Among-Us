import pyautogui
import time
import win32api, win32con
import keyboard

#Automate Among Us Wires

#finds pos of the blue wires pieces
def findBlue(pos):
    try:
        if pos == 'left':
            x,y = pyautogui.locateCenterOnScreen('blueWireLeft.png', confidence=0.8)
            return x,y
        if pos == 'right':
            x,y = pyautogui.locateCenterOnScreen('blueWireRight.png', confidence=0.8)
            return x,y 
    except:
        pass     

#Finds red wirs pieces
def findRed(pos):
    try:
        if pos == 'left':
            x,y = pyautogui.locateCenterOnScreen('redWireLeft.png', confidence=0.8)
            return x,y
        if pos == 'right':
            x,y = pyautogui.locateCenterOnScreen('redWireRight.png', confidence=0.8)
            return x,y 
    except:
        pass 

#Finds yellow wires pieces
def findYellow(pos):
    try:
        if pos == 'left':
            x,y = pyautogui.locateCenterOnScreen('yellowWireLeft.png', confidence=0.8)
            return x,y
        if pos == 'right':
            x,y = pyautogui.locateCenterOnScreen('yellowWireRight.png', confidence=0.8)
            return x,y 
    except:
        pass 

#Finds pink wires pieces
def findPink(pos):
    try:
        if pos == 'left':
            x,y = pyautogui.locateCenterOnScreen('pinkWireLeft.png', confidence=0.8)
            return x,y
        if pos == 'right':
            x,y = pyautogui.locateCenterOnScreen('pinkWireRight.png', confidence=0.8)
            return x,y 
    except:
        pass 

#Runs the program until you press 'q'
while keyboard.is_pressed('q') == False:

    b_left = findBlue('left')
    b_right = findBlue('right')
    if b_left != None:
        try:
            pyautogui.moveTo(b_left[0], b_left[1])
            pyautogui.drag((b_right[0] - b_left[0]), (b_right[1] - b_left[1]), duration=0.5)
        except:
            pass
    
    r_left = findRed('left')
    r_right = findRed('right')
    if r_left != None:
        try:
            pyautogui.moveTo(r_left[0], r_left[1])
            pyautogui.drag((r_right[0] - r_left[0]), (r_right[1] - r_left[1]), duration=0.5)
        except:
            pass
    
    y_left = findYellow('left')
    y_right = findYellow('right')
    if y_left != None:
        try:
            pyautogui.moveTo(y_left[0], y_left[1])
            pyautogui.drag((y_right[0] - y_left[0]), (y_right[1] - y_left[1]), duration=0.5)
        except:
            pass
    
    p_left = findPink('left')
    p_right = findPink('right')
    if p_left != None:
        try:
            pyautogui.moveTo(p_left[0], p_left[1])
            pyautogui.drag((p_right[0] - p_left[0]), (p_right[1] - p_left[1]), duration=0.5)
        except:
            pass



