import pyautogui
import time
import cv2
from twilio.rest import Client
#bot used to tell me when FCW or Graybeech are online
# (must be in Uswest3 nexus)
# will get the trade guranteed
#print(pyautogui.position())
#692, 519 top left
#top right 721 520
#bot right 723 550
#pyautogui.click(603,700)
#im1 = pyautogui.screenshot(region=(692, 519, 30, 30))
#im2 = pyautogui.screenshot('my_sscreenshot.png')


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
    
#switch_back()
#vault_inv()
#inv_vault()



while True:
    #pyautogui.click(800,400)
    g = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/gray.png')
    f = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/FCW.png')
    if g != None or f!=None:
        client = Client("ACf3d6e998fce70398ba2e11c55f99d441", "0759088a22e0e6e81ff17a0729ef1348")
        client.messages.create(to="+17326103038", 
                            from_="+12513062877", 
                            body="GrayBeech/FCW is online!")
    #k = pyautogui.locateOnScreen('my_sscreenshot.png')
    #print(k)

    
    if g != None:
        pyautogui.typewrite(["enter"])
        pyautogui.typewrite("/trade graybeech")
    if f != None:
        pyautogui.typewrite(["enter"])
        pyautogui.typewrite("/trade FCWLQgtgEX")


    #pyautogui.click(logScreenshot='/Users/edmond/Desktop/ROTMGBot#1/test4.png')
    success = False
    while g != None:
        if success == True:
            pyautogui.typewrite(["enter"])
            pyautogui.typewrite("/trade graybeech")
        #print("found person")
        if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/beechR.png') != None:
            #print("message received")
            #print("oh")
            time.sleep(5.2)
            #pyautogui.click(603,723)
            pyautogui.typewrite(["enter"])
            time.sleep(6)
            success = True
            if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/S_B.png') != None:
                time.sleep(10)
                switch_back()
                time.sleep(5)
        else:
            success = False
        #print("in gray")
        
    Success = False
    while f != None:
        #print("work")
        if Success == True:
            pyautogui.typewrite(["enter"])
            pyautogui.typewrite("/trade FCWLQgtgEX")
        #print("found person")
        if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/fcwD.png') != None:
            #print("message received")
            time.sleep(5.0)
            pyautogui.typewrite(["enter"])
            time.sleep(4.5)
            Success = True
            if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/S_B.png') != None:
                time.sleep(10)
                switch_back()
                time.sleep(5)
        else:
            Success = False
        #print("in FCW")
    #print("none located, trying again")
#953,512 1
#998,512 2
#1086 556 8

#33 units x
#44 units y
        
        #d = pyautogui.center(k)
        #print(d)
        #s = list(d)
        #pyautogui.moveTo(s[0], s[1], duration = 2)
        #pyautogui.click()
        #pyautogui.click(348,577)
    