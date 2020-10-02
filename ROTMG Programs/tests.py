import pyautogui
import time
import cv2
from twilio.rest import Client
#must have six tabs open
#can go afk
import pyautogui
import time
import cv2
from twilio.rest import Client


def inv_vault(): 
    xCoords = []
    yCoords = []
    chestLocs = list(pyautogui.locateAllOnScreen('/Users/edmond/Desktop/ROTMGBot#1/openchest.png', confidence = 0.95))
    print(len(chestLocs))
    for chest in chestLocs:
        print(str(chest[0]) + " " +  str(chest[1]))
        xCoords.append(int(chest[0]+20))
        yCoords.append(int(chest[1]+20))
    print(xCoords)
    print(yCoords)
    pyautogui.click(xCoords[7], yCoords[7])
    time.sleep(1)
    pyautogui.hotkey('space')
    time.sleep(1)
    x = 953
    y = 512
    i = 0
    counter = 0
    for i in range(8):
        if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/blank2.png', confidence = 0.97) != None: 
            print('detected a blank')
            pyautogui.click(x,y)
            time.sleep(0.25)
            pyautogui.dragTo(900, 530, 0.40, button='left')
            if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/blankinv.png') != None: 
                return
            x+=44
            if i == 3:
                y+=44
                x = 953
        else:
            i = 0
            pyautogui.keyDown('d')
            time.sleep(0.1)
            pyautogui.keyUp('d')
            counter += 1    
            if counter > 4 and pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/blankinv.png') == None: 
                return False #TURN OFF PROGRAM
                print('there is no blank inv after inv_vault')

def main():
    inv_vault()
    time.sleep(1)

main()