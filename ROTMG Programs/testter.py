import pyautogui
import time
import cv2
from twilio.rest import Client

def startRecord():
    pyautogui.keyDown('shift')
    pyautogui.keyDown('command')
    pyautogui.keyDown('5')    
    pyautogui.keyUp('shift')
    pyautogui.keyUp('command')
    pyautogui.keyUp('5')

    time.sleep(2)
    record = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/record.png', confidence = 0.45)
    if record != None:
        record = pyautogui.center(record)
        recordX, recordY = record
        pyautogui.click(recordX, recordY)
        time.sleep(1)
        pyautogui.click(800,400)
        print("does this")
    else:
        pyautogui.hotkey('esc')
        print('not this')

def stopRecord():
    pyautogui.moveTo(923,0)
    time.sleep(1)
    stop = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/stop!.png', confidence = 0.55)
    if stop != None:
        stop = pyautogui.center(stop)
        stopX, stopY = stop
        pyautogui.click(stopX, stopY)
        time.sleep(1)
        pyautogui.click(800,400)

def returnToVault():
    x=0
    while True:
        record = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/vault3.png', confidence = 0.75)
        if record != None:
            record = pyautogui.center(record)
            recordX, recordY = record
            pyautogui.click(recordX, recordY)
            pyautogui.hotkey('space')
            time.sleep(2)
            pyautogui.hotkey('shift')
            time.sleep(5)
            pyautogui.typewrite('z')
            time.sleep(0.2)
            pyautogui.typewrite('w')
            pyautogui.typewrite('w')
            time.sleep(0.2)
            pyautogui.typewrite('w')
            time.sleep(0.2)
            pyautogui.typewrite('w')
            time.sleep(0.2)
            pyautogui.typewrite('w')
            time.sleep(0.2)
            pyautogui.typewrite('w')


            #time.sleep(0.02)
            #pyautogui.keyUp('w')
            break
        else: 
            print("vault not found")
            x+=1
        if x == 3:
            pyautogui.keyDown('e')
            time.sleep(0.25)
            pyautogui.keyUp('e')
            x=0

def sendAmanda():
    pyautogui.keyDown('command')
    pyautogui.keyDown('tab')
    pyautogui.keyUp('command')
    pyautogui.keyUp('tab')
    time.sleep(1)
    pyautogui.click(1377,58)
    time.sleep(1)
    pyautogui.hotkey("command", "c")
    mess = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/messageSymbol.png', confidence = 0.85)
    if mess != None:
        mess = pyautogui.center(mess)
        messX, messY = mess
        pyautogui.click(messX, messY)
    time.sleep(3)
    a1 = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/en1.png', confidence = 0.85)
    a2 = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/en2.png', confidence = 0.85)
    if a2 != None:
        a2 = pyautogui.center(a2)
        ax, ay = a2
        pyautogui.click(ax, ay)
    if a1 != None:
        a1 = pyautogui.center(a1)
        ax, ay = a1
        pyautogui.click(ax, ay)
    pyautogui.click(567,828)
    time.sleep(1)
    pyautogui.hotkey('command', 'v')
    pyautogui.hotkey('enter')
    time.sleep(1)
    pyautogui.click(567, 400)
    pyautogui.hotkey('command', 'w')
    time.sleep(1)
    pyautogui.click(1377,58)
    pyautogui.dragTo(1388, 900,2,button='left') 
    chrome = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/chrome.png', confidence = 0.75)
    if chrome != None:
        chrome = pyautogui.center(chrome)
        cx, cy = chrome
        pyautogui.click(cx, cy)



def inv_vaultD(): 
    x = 953
    y = 512
    for i in range(0,8):
        if i == 0:
            pyautogui.click(x,y)
            time.sleep(0.25)
            pyautogui.dragTo(900, 530, 0.40, button='left')
        if i == 1 or i == 2 or i == 3:
            ix = 982
            iy =495
            im = pyautogui.screenshot(region=(ix,iy, 33, 33))
            print('im:', im)
            deca = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/deca2.png', confidence = 0.95)
            if im == deca:
                print("its a deca that is at location: ", i)
            else:
                pyautogui.keyDown('command')
                time.sleep(1)
                pyautogui.click(x,y)
                time.sleep(1)
                pyautogui.keyUp('command')
                ix += 45
        x+=44
        if i == 3:
            y+=44
            x = 953

def replenish(): #must be after returntovault
    xCoords = []
    yCoords = []
    chestLocs = list(pyautogui.locateAllOnScreen('/Users/edmond/Desktop/ROTMGBot#1/openchest.png', confidence = 0.95))
    for chest in chestLocs:
        print(str(chest[0]) + " " +  str(chest[1]))
        xCoords.append(int(chest[0]+20))
        yCoords.append(int(chest[1]+20))
    print(xCoords)
    print(yCoords)
    x = 0
    deca1 = xCoords[x], yCoords[x] 
    x += 1
    deca2 = xCoords[x], yCoords[x] 
    x += 1
    ether1 = xCoords[x], yCoords[x] 
    x += 1
    ether2 = xCoords[x], yCoords[x] 
    x += 1
    ether3 = xCoords[x], yCoords[x] 
    x += 1
    pixie1 = xCoords[x], yCoords[x] 
    x += 1
    pixie2 = xCoords[x], yCoords[x] 
    x += 1
    pixie3 = xCoords[x], yCoords[x] 
    x += 2
    resetLoc = xCoords[x], yCoords[x]

    
    pyautogui.click(ether1) #starting position
    pyautogui.hotkey('space')
    time.sleep(2)
    if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/decaU.png', confidence = 0.95) == None:
        vault_invD()
    pyautogui.keyDown('d')
    time.sleep(0.1)
    pyautogui.keyUp('d')
    if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/decaU.png', confidence = 0.95) == None:
        vault_invD()
    pyautogui.keyDown('d')
    time.sleep(0.1)
    pyautogui.keyUp('d')  
    if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/decaU.png', confidence = 0.95) == None:
        vault_invD() 
    pyautogui.keyDown('d')
    time.sleep(0.1)
    pyautogui.keyUp('d')
    if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/decaU.png', confidence = 0.95) == None:
        vault_invD() 
    pyautogui.keyDown('d')
    time.sleep(0.1)
    pyautogui.keyUp('d')   
#ether time
    if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/etherU.png', confidence = 0.95) == None:
        vault_invE() 
    pyautogui.keyDown('s')
    time.sleep(0.1)
    pyautogui.keyUp('s')
    if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/etherU.png', confidence = 0.95) == None:
        vault_invE() 
    pyautogui.keyDown('a')
    time.sleep(0.1)
    pyautogui.keyUp('a')
#pixie time
    if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/pixieU.png', confidence = 0.95) == None:
        vault_invP() 
    pyautogui.keyDown('a')
    time.sleep(0.1)
    pyautogui.keyUp('a')
    if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/pixieU.png', confidence = 0.95) == None:
        vault_invP() 
    pyautogui.keyDown('a')
    time.sleep(0.1)
    pyautogui.keyUp('a')
    #if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/pixieU.png', confidence = 0.95) == None:
    #    vault_invP() 
    #pyautogui.keyDown('a')
    #time.sleep(0.1)
    #pyautogui.keyUp('a')
    if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/FULLINV.png') == None:
        print('inv is not full')
        pyautogui.keyDown('shift')
        pyautogui.keyDown('command')
        pyautogui.keyDown('3')
        pyautogui.keyUp('shift')
        pyautogui.keyUp('command')
        pyautogui.keyUp('3')
        return False
        
def screenie():
    pyautogui.keyDown('shift')
    pyautogui.keyDown('command')
    pyautogui.keyDown('3')
    pyautogui.keyUp('shift')
    pyautogui.keyUp('command')
    pyautogui.keyUp('3')

def Communicator():
    pyautogui.click(350,700)
    pyautogui.hotkey('tab')
    pyautogui.typewrite("hi. are you selling me a skin that i posted on my realmeye")
    pyautogui.keyDown('shift') 
    pyautogui.typewrite('/ ')
    pyautogui.keyUp('shift')
    pyautogui.typewrite('in all capital, type ')
    pyautogui.keyDown('shift') 
    pyautogui.typewrite('yyy ')
    pyautogui.keyUp('shift')
    pyautogui.typewrite("if yes or ")
    pyautogui.keyDown('shift') 
    pyautogui.typewrite('nnn ')
    pyautogui.keyUp('shift')
    pyautogui.typewrite("if no.")
    pyautogui.hotkey('enter')

    time.sleep(22)
    count = 0
    loop = True
    while loop:
        if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/YYY.png', confidence = 0.85) != None: 
            pyautogui.hotkey('tab')
            time.sleep(1)
            pyautogui.typewrite("ok. as payment, type ")
            pyautogui.keyDown('shift') 
            pyautogui.typewrite('ppp ')
            pyautogui.keyUp('shift')
            pyautogui.typewrite('if you want pixies, type ')
            pyautogui.keyDown('shift') 
            pyautogui.typewrite('eee ')
            pyautogui.keyUp('shift')
            pyautogui.typewrite('for etherites, type ')
            pyautogui.keyDown('shift') 
            pyautogui.typewrite('ddd ')
            pyautogui.keyUp('shift')
            pyautogui.typewrite('for decas.')

            pyautogui.hotkey('enter')
            pyautogui.hotkey('tab')
            time.sleep(1)
            pyautogui.typewrite("i am only offering decas/pixies/etherites in their respective quantities. type ")
            pyautogui.keyDown('shift') 
            pyautogui.typewrite('xxx ')
            pyautogui.keyUp('shift')
            pyautogui.typewrite("if you do not want to trade.")
            pyautogui.hotkey('enter')
            pyautogui.hotkey('tab')
            time.sleep(2)
            pyautogui.typewrite("you have 30 seconds to respond with one of the options.")
            pyautogui.hotkey('enter')
            loop = False

        elif pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/NNN.png', confidence = 0.85) != None: 
            pyautogui.hotkey('tab')
            time.sleep(1)
            pyautogui.typewrite("ok. have a good day.")
            pyautogui.hotkey('enter')
            time.sleep(5)
            return False

        else:
            pyautogui.hotkey('tab')
            pyautogui.typewrite("you have not chosen a response yet.")
            pyautogui.hotkey('enter')
            time.sleep(15)
            count+=1
            print("count: ", count)
            if count > 2: #20 + 15 = 35 seconds wait for response
                pyautogui.hotkey('tab')
                pyautogui.typewrite("you have not chosen a response. try again in a few minutes if you still want to trade. goodbye.")
                pyautogui.hotkey('enter')
                loop = False
                return False
        print("still in loop checking for response")



def main():
    #startRecord()
    #time.sleep(5)
    #stopRecord()
    #while True:
        #returnToVault()
        #time.sleep(2)
        #pyautogui.typewrite('r')
        #time.sleep(3)
    #x, y = pyautogui.locateCenterOnScreen('vault.png')
    #pyautogui.click(x, y)
    #pyautogui.hotkey('space')
    #pyautogui.hotkey('shift')
    #while True:
     #   returnToVault()
    print(pyautogui.position())
main()