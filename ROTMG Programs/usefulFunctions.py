import pyautogui
import time

def usw3Trader():
    loop = True
    while loop:
        pyautogui.hotkey('enter')
        pyautogui.hotkey('command', 'v')
        pyautogui.hotkey('enter')
        request = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/accept.png', confidence = 0.85)
        if request != None:
            request = pyautogui.center(request)
            requestX, requestY = request
            pyautogui.click(requestX, requestY)
            while pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/trading?.png', confidence = 0.85) != None or pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/trde?.png', confidence = 0.85) != None:
                time.sleep(5)
        time.sleep(3)
                    

#When Function Called: switches items from backpack to inventory and vice versa
def switch_back():
    x = 953
    y = 512
    pyautogui.keyDown('command')
    for i in range(7):
        time.sleep(0.5)
        pyautogui.click(x,y)
        x+=42
        if i == 3:
            y+=46
            x = 953

#When Function Called: switches items from vault to inventory
def vault_inv():
    x = 953
    y = 639
    for i in range(8):
        time.sleep(.5)
        pyautogui.click(x,y,2)
        x+=42
        if i == 3:
            y+=46
            x = 953

#When Function Called: switches item from inventory to vault
def inv_vault(): 
    x = 953
    y = 512
    for i in range(8):
        pyautogui.click(x,y)
        time.sleep(0.25)
        pyautogui.dragTo(900, 530, 0.40, button='left')
        x+=44
        if i == 3:
            y+=44
            x = 953


usw3Trader()

