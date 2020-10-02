import PyAutoGUI
import time
import cv2
from twilio.rest import Client
#must have six tabs open
#can go afk
import pyautogui
import time
import cv2
from twilio.rest import Client

#checklist 
'''
- make sure inv is 4 decas 2 ethers 2 pixies
- make sure vaults are in order : 4 decas vaults 2 ethers vaults 2 pixies vaults
- make sure pots are in order (6 hp pots, 5 mp pots)
- makes sure in ASE server
- make sure realmeye offers are up and correct
- make sure nothing is open on home window except for VS code
- make sure computer is plugged in
- make sure the deposit two vaults are empty
- make sure recording config is ready

things i still need to work on:
- what if two people message me at the same time?
- conduct multiple trades at once
- if someone cancels the trade and trades with me again, accept it and start the whole process over (do multiple revised_skintradeD's if trading? is not found )

Bigger: (machine learning)
- find out how to make something that can analyze when are good times to sell skins and when are good times to buy skins and which skins to sell and which skins to buy
- how to make the bot more human-like
'''



def checkwhisperNotReady():
    if pyautogui.pixelMatchesColor(350, 700, (0, 92, 97)) == True or pyautogui.pixelMatchesColor(350, 680, (0, 92, 97)) == True:
        print("whisper found")
        counter = 0
        found = True
        while found:
            pyautogui.hotkey('tab')
            time.sleep(1)
            pyautogui.typewrite("i am currently in the middle of a trade, or finishing one up. please message me after 2 minutes to try again.")
            pyautogui.hotkey('enter')
            time.sleep(1)
            if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/notread2.png', confidence = 0.65) == None:
                found = False
                print('message found')
            else:
                print('m not f')
                time.sleep(3)
                counter += 1
                if counter == 3:
                    found = False
                    return

        

def screenie():
    pyautogui.keyDown('shift')
    pyautogui.keyDown('command')
    pyautogui.keyDown('3')
    pyautogui.keyUp('shift')
    pyautogui.keyUp('command')
    pyautogui.keyUp('3')

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
        #pyautogui.click(800,400)
        pyautogui.keyDown('command')
        pyautogui.keyDown('tab')
        pyautogui.keyUp('command')
        pyautogui.keyUp('tab')
        time.sleep(5)
        pyautogui.click(1377,50)
        pyautogui.dragTo(1388, 250,2,button='left') 
        chrome = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/chrome.png', confidence = 0.75)
        if chrome != None:
            chrome = pyautogui.center(chrome)
            cx, cy = chrome
            pyautogui.click(cx, cy)
            pyautogui.click(cx, cy)

        

def sendAmanda():
    pyautogui.keyDown('command')
    pyautogui.keyDown('tab')
    pyautogui.keyUp('command')
    pyautogui.keyUp('tab')
    time.sleep(1)
    pyautogui.click(1377,58)
    time.sleep(1)
    pyautogui.hotkey("command", "c")
    mess = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/msymbol.png', confidence = 0.75)
    if mess != None:
        mess = pyautogui.center(mess)
        messX, messY = mess
        pyautogui.click(messX, messY)
        print('did messages get clicked')
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
    pyautogui.keyDown('command')
    pyautogui.keyDown('w')
    pyautogui.keyUp('command')
    pyautogui.keyUp('w')
    time.sleep(1)
    pyautogui.click(1377,58)
    pyautogui.dragTo(1388, 500,2,button='left') 
    chrome = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/chrome.png', confidence = 0.75)
    if chrome != None:
        chrome = pyautogui.center(chrome)
        cx, cy = chrome
        pyautogui.click(cx, cy)
        pyautogui.click(cx, cy)
    time.sleep(1)

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
def vault_invE():
    x = 953
    y = 639
    for i in range(8):
        time.sleep(.5)
        pyautogui.click(x,y,2)
        x+=42
        if i == 3:
            y+=46
            x = 953
        if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/etherU.png', confidence = 0.95) != None:
            return

def vault_invP():
    x = 953
    y = 639
    for i in range(8):
        time.sleep(.5)
        pyautogui.click(x,y,2)
        x+=42
        if i == 3:
            y+=46
            x = 953
        if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/pixieU.png', confidence = 0.95) != None:
            return      
        
def vault_invD():
    x = 953
    y = 639
    for i in range(8):
        time.sleep(.5)
        pyautogui.click(x,y,2)
        x+=42
        if i == 3:
            y+=46
            x = 953
        if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/decaU.png', confidence = 0.95) != None:
            return
        

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

def inv_vaultD(): #needs work
    x = 953
    y = 512
    for i in range(0,8):
        if i == 0:
            pyautogui.click(x,y)
            time.sleep(0.25)
            pyautogui.dragTo(900, 530, 0.40, button='left')
        decas = list(pyautogui.locateAllOnScreen('/Users/edmond/Desktop/ROTMGBot#1/deca2.png', confidence = 0.85))
        numD = len(decas)
        if numD == 1:
            if i == 1 or i == 2:
                pyautogui.keyDown('command')
                time.sleep(1)
                pyautogui.click(x,y)
                time.sleep(1)
                pyautogui.keyUp('command')
        if numD == 2:
            if i == 1:
                pyautogui.keyDown('command')
                time.sleep(1)
                pyautogui.click(x,y)
                time.sleep(1)
                pyautogui.keyUp('command')
        if numD == 3:
            pass
        x+=44
        if i == 3:
            y+=44
            x = 953

def inv_vaultE(): 
    x = 953
    y = 512
    for i in range(8):
        if i ==4:
            pyautogui.click(x,y)
            time.sleep(0.25)
            pyautogui.dragTo(900, 530, 0.40, button='left')
        if i == 5 and pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/etherite.png', confidence = 0.85) == None:
            pyautogui.keyDown('command')
            time.sleep(1)
            pyautogui.click(x,y)
            time.sleep(1)
            pyautogui.keyUp('command')
        x+=44
        if i == 3:
            y+=44
            x = 953

def inv_vaultP(): 
    x = 953
    y = 512
    for i in range(8):
        if i == 6:
            pyautogui.click(x,y)
            time.sleep(0.25)
            pyautogui.dragTo(900, 530, 0.40, button='left')
        if i == 7 and pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/1pixie.png', confidence = 0.85) == None:
            pyautogui.keyDown('command')
            time.sleep(1)
            pyautogui.click(x,y)
            time.sleep(1)
            pyautogui.keyUp('command')
        x+=44
        if i == 3:
            y+=44
            x = 953

def depositD(): #must be after returntoVault
    checkwhisperNotReady()
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

    pyautogui.click(deca1)
    pyautogui.hotkey('space')
    time.sleep(3)
    if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/blank2.png') != None:
        inv_vaultD()
    pyautogui.keyDown('d')
    time.sleep(0.1)
    pyautogui.keyUp('d')
    if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/blank2.png') != None:
        inv_vaultD()
    else:
        screenie()
        return False

        #print("program must stop") 
        #stop program

    time.sleep(3)
    checkwhisperNotReady()
    time.sleep(1)
    pyautogui.typewrite('r')
    if returnToVault() == False:
        return False

def depositE(): #must be after returntoVault
    checkwhisperNotReady()
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

    pyautogui.click(deca1)
    pyautogui.hotkey('space')
    time.sleep(3)
    if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/blank2.png') != None:
        inv_vaultE()
    pyautogui.keyDown('d')
    time.sleep(0.1)
    pyautogui.keyUp('d')
    if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/blank2.png') != None:
        inv_vaultE()
    else:
        screenie()
        return False #program must stop

    time.sleep(3)
    checkwhisperNotReady()
    time.sleep(1)
    pyautogui.typewrite('r')
    if returnToVault() == False:
        return False

def depositP(): #must be after returntoVault
    checkwhisperNotReady()
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

    pyautogui.click(deca1)
    time.sleep(3)
    pyautogui.hotkey('space')
    if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/blank2.png') != None:
        inv_vaultP()
    pyautogui.keyDown('d')
    time.sleep(0.1)
    pyautogui.keyUp('d')
    if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/blank2.png') != None:
        inv_vaultP()
    else:
        screenie()
        return False
        #print("program must stop") 
        #stop program

    time.sleep(3)
    checkwhisperNotReady()
    time.sleep(1)
    pyautogui.typewrite('r')
    if returnToVault() == False:
        return False

def replenish(): #must be after returntovault
    checkwhisperNotReady()
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
    '''
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
    '''
    
    pyautogui.click(ether1) #starting position
    pyautogui.hotkey('space')
    time.sleep(2)
    if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/decaU.png', confidence = 0.95) == None and pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/emptyVault.png', confidence = 0.95) == None:
        vault_invD()
    pyautogui.keyDown('d')
    time.sleep(0.1)
    pyautogui.keyUp('d')
    if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/decaU.png', confidence = 0.95) == None and pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/emptyVault.png', confidence = 0.95) == None:
        vault_invD()
    pyautogui.keyDown('d')
    time.sleep(0.1)
    pyautogui.keyUp('d')  
    if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/decaU.png', confidence = 0.95) == None and pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/emptyVault.png', confidence = 0.95) == None:
        vault_invD() 
    pyautogui.keyDown('d')
    time.sleep(0.1)
    pyautogui.keyUp('d')
    if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/decaU.png', confidence = 0.95) == None and pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/emptyVault.png', confidence = 0.95) == None:
        vault_invD() 
    pyautogui.keyDown('d')
    time.sleep(0.1)
    pyautogui.keyUp('d') 
    checkwhisperNotReady()  
#ether time
    if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/etherU.png', confidence = 0.95) == None and pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/emptyVault.png', confidence = 0.95) == None:
        vault_invE() 
    pyautogui.keyDown('s')
    time.sleep(0.1)
    pyautogui.keyUp('s')
    if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/etherU.png', confidence = 0.95) == None and pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/emptyVault.png', confidence = 0.95) == None:
        vault_invE() 
    pyautogui.keyDown('a')
    time.sleep(0.1)
    pyautogui.keyUp('a')
    checkwhisperNotReady()
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
    checkwhisperNotReady()
    #if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/pixieU.png', confidence = 0.95) == None:
    #    vault_invP() 
    #pyautogui.keyDown('a')
    #time.sleep(0.1)
    #pyautogui.keyUp('a')
    pyautogui.click(350,700) #RIGHT HERE
    if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/FULLINV.png') == None: 
        print('inv is not full')
        screenie()
        return False

    time.sleep(1)
        
    
    pyautogui.typewrite("r")
    if returnToVault() == False:
        return False
    




'''
    #pyautogui.click(ether3)
    #pyautogui.hotkey('space')
    etherU = pyautogui.locateCenterOnScreen('/Users/edmond/Desktop/ROTMGBot#1/etherU.png', confidence = 0.85)
    if etherU == None:
        print("need ethers")
        #ether1 = pyautogui.center(ether1)
        #ether1X, ether1Y = ethe r1
        pyautogui.click(ether1)
        pyautogui.hotkey("space")
        vault_invE()
        pyautogui.click(resetLoc)
        pyautogui.hotkey("space")
        if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/etherU.png', confidence = 0.85) == None:
            pyautogui.click(ether2)
            pyautogui.hotkey("space")
            vault_invE()
            pyautogui.click(resetLoc)
            pyautogui.hotkey("space")
            if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/etherU.png', confidence = 0.85) == None:
                pyautogui.click(ether3)
                pyautogui.hotkey("space")
                vault_invE()
                pyautogui.click(resetLoc)
                pyautogui.hotkey("space")
    
        print("onto the next item")

    else:
        print("have all my ethers")
    #if my inv is not full
    #go to one of the vaults
    #do one increment V_I, check if full, then continue until full
    #do backpack
    #do other items
    #go back to starting position
'''


def fullreset():
    #startRecord()
    screenie()
    for i in range (0,15): 
        pyautogui.click(700,195)
        time.sleep(1)
        
        play2 = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/play2.png', confidence = 0.65)
        if play2 != None:
            play2 = pyautogui.center(play2)
            play2X, play2Y = play2
            time.sleep(1)
            pyautogui.click(play2X, play2Y)
            time.sleep(10)
            if returnToVault2() == False:
                return False
            print('this should run') 
            screenie()
            #stopRecord()
            client = Client("ACf3d6e998fce70398ba2e11c55f99d441", "0759088a22e0e6e81ff17a0729ef1348")
            client.messages.create(to="+17326103038", 
                                from_="+12513062877", 
                                body="full reset started but interrupted by the play button being found again! yay")
            return 
        
        update = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/update.png', confidence = 0.65)
        if update != None:
            update = pyautogui.center(update)
            uX, uY = update
            time.sleep(1)
            pyautogui.click(uX, uY) 
            time.sleep(10)
            chrome = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/chrome.png', confidence = 0.75)
            if chrome != None:
                chrome = pyautogui.center(chrome)
                cx, cy = chrome
                pyautogui.click(cx, cy)
                pyautogui.click(cx, cy)
            #stopRecord()
            client = Client("ACf3d6e998fce70398ba2e11c55f99d441", "0759088a22e0e6e81ff17a0729ef1348")
            client.messages.create(to="+17326103038", 
                                from_="+12513062877", 
                                body="full reset started but interrupted by the update being found (and remind me later) button being clicked! yay")
            return

        time.sleep(18)
    screenie()
    client = Client("ACf3d6e998fce70398ba2e11c55f99d441", "0759088a22e0e6e81ff17a0729ef1348")
    client.messages.create(to="+17326103038", 
                        from_="+12513062877", 
                        body="full reset in progress! 5 minutes passed since something malfunctioned")
    time.sleep(1)
    pyautogui.click(142,448)
    pyautogui.hotkey('command', 'r')
    time.sleep(30) #wait for realm to load
    screenie()
    logIn = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/logIn1.png', confidence = 0.95)
    login2 = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/login2.png', confidence = 0.95)
    logged = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/loggedin.png', confidence = 0.85)
    if logIn != None:
        log = pyautogui.center(logIn)
        lX, lY = log
        time.sleep(1)
        pyautogui.click(lX, lY)
        time.sleep(1)
        pyautogui.click(657,350)
        time.sleep(1)
        pyautogui.typewrite('eddietgh1')
        time.sleep(1)
        pyautogui.hotkey('shift', '2')
        time.sleep(1)
        pyautogui.typewrite('gmail.com')
        time.sleep(1)
        pyautogui.click(662,419)
        time.sleep(1)
        pyautogui.typewrite('101edmondus101')
        time.sleep(1)
        pyautogui.hotkey('enter')
        time.sleep(15)
        screenie()
        play = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/play.png', confidence = 0.65)
        if play != None:
            play = pyautogui.center(play)
            playX, playY = play
            time.sleep(1)
            pyautogui.click(playX, playY)
            time.sleep(2)
        play2 = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/play2.png', confidence = 0.65)
        if play2 != None:
            play2 = pyautogui.center(play2)
            play2X, play2Y = play2
            time.sleep(1)
            pyautogui.click(play2X, play2Y)
            time.sleep(10)
        print('about to go to vault')
        screenie()
        if returnToVault2() == False:
            print('unable to return to vault after trying to full reset')
            #stopRecord()
            client = Client("ACf3d6e998fce70398ba2e11c55f99d441", "0759088a22e0e6e81ff17a0729ef1348")
            client.messages.create(to="+17326103038", 
                                from_="+12513062877", 
                                body="vault is not found after trying to full reset. program should shut off soon")
    
            return False
            #once = True
            #send message to my phone here
            #if returnToVault2() == False and once == True:
                #print('unable for the second time')
                #return False
        else: 
            #stopRecord()
            client = Client("ACf3d6e998fce70398ba2e11c55f99d441", "0759088a22e0e6e81ff17a0729ef1348")
            client.messages.create(to="+17326103038", 
                                from_="+12513062877", 
                                body="vault is found after trying to full reset.")

            return
        
    elif login2 != None:
        login2 = pyautogui.center(login2)
        lX2, lY2 = log2
        time.sleep(1)
        pyautogui.click(lX2, lY2)
        time.sleep(1)
        pyautogui.click(657,350)
        time.sleep(1)
        pyautogui.typewrite('eddietgh1')
        time.sleep(1)
        pyautogui.hotkey('shift', '2')
        time.sleep(1)
        pyautogui.typewrite('gmail.com')
        time.sleep(1)
        pyautogui.click(662,419)
        time.sleep(1)
        pyautogui.typewrite('101edmondus101')
        time.sleep(1)
        pyautogui.hotkey('enter')
        time.sleep(15)
        screenie()
        #play = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/play.png', confidence = 0.65)
        #if play != None:
            #play = pyautogui.center(play)
            #playX, playY = play
            #pyautogui.click(playX, playY)
            #time.sleep(2)
        play2 = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/play2.png', confidence = 0.65)
        if play2 != None:
            play2 = pyautogui.center(play2)
            play2X, play2Y = play2
            time.sleep(1)
            pyautogui.click(play2X, play2Y)
            time.sleep(10)
        print('about to go to vault')
        screenie()
        if returnToVault2() == False:
            print('unable to return to vault after trying to full reset')
            #send message to my phone here
            client = Client("ACf3d6e998fce70398ba2e11c55f99d441", "0759088a22e0e6e81ff17a0729ef1348")
            client.messages.create(to="+17326103038", 
                                from_="+12513062877", 
                                body="vault is not found after trying to full reset. program should shut off soon")

            #stopRecord()
            return False
        else:
            client = Client("ACf3d6e998fce70398ba2e11c55f99d441", "0759088a22e0e6e81ff17a0729ef1348")
            client.messages.create(to="+17326103038", 
                                from_="+12513062877", 
                                body="vault is found after trying to full reset.")

            #stopRecord()
            return
    elif logged != None:
        screenie()
        play = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/play.png', confidence = 0.65)
        if play != None:
            play = pyautogui.center(play)
            playX, playY = play
            time.sleep(1)
            pyautogui.click(playX, playY)
            time.sleep(2)
        play2 = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/play2.png', confidence = 0.65)
        if play2 != None:
            play2 = pyautogui.center(play2)
            play2X, play2Y = play2
            time.sleep(1)
            pyautogui.click(play2X, play2Y)
            time.sleep(10)
        print('about to go to vault')
        screenie()
        if returnToVault2() == False:
            client = Client("ACf3d6e998fce70398ba2e11c55f99d441", "0759088a22e0e6e81ff17a0729ef1348")
            client.messages.create(to="+17326103038", 
                                from_="+12513062877", 
                                body="vault is not found after trying to full reset. program should shut off soon")
            print('unable to return to vault after trying to full reset')
            #send message to my phone here
            #stopRecord()
            return False
        else:
            client = Client("ACf3d6e998fce70398ba2e11c55f99d441", "0759088a22e0e6e81ff17a0729ef1348")
            client.messages.create(to="+17326103038", 
                                from_="+12513062877", 
                                body="vault is found after trying to full reset.")

            #stopRecord()
            return
    else:
        #stopRecord()
        client = Client("ACf3d6e998fce70398ba2e11c55f99d441", "0759088a22e0e6e81ff17a0729ef1348")
        client.messages.create(to="+17326103038", 
                            from_="+12513062877", 
                            body="The homepage of rotmg has not been reached after a fullreset...")

        return False



def goKeys():
    time.sleep(3)
    pyautogui.keyDown('a')
    time.sleep(0.9)
    pyautogui.keyUp('a')
    pyautogui.keyDown('w')
    time.sleep(0.6)
    pyautogui.keyUp('w')

def reset2():
    time.sleep(3)
    pyautogui.keyDown('s')
    time.sleep(0.6)
    pyautogui.keyUp('s')
    pyautogui.keyDown('d')
    time.sleep(0.9)
    pyautogui.keyUp('d')
    returnToVault() #if this vault fails the program wont recognize
        

def reset():
    print("I am now resettting")
    pyautogui.typewrite('o')
    time.sleep(1)
    home = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/home.png', confidence = 0.85)
    if home != None:
        home = pyautogui.center(home)
        homeX, homeY = home
        time.sleep(1)
        pyautogui.click(homeX, homeY)
    time.sleep(10)

    play = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/play.png', confidence = 0.65)
    if play != None:
        play = pyautogui.center(play)
        playX, playY = play
        time.sleep(1)
        pyautogui.click(playX, playY)
        time.sleep(5)

    if returnToVault() == False:
        return False

def acceptTradeRequest():
    request = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/accept.png', confidence = 0.85)
    if request != None:
        request = pyautogui.center(request)
        requestX, requestY = request
        time.sleep(1)
        pyautogui.click(requestX, requestY)
        time.sleep(2)
        if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/trade?.png', confidence = 0.75) != None or pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/trde?.png', confidence = 0.75) != None:
            print("I AM IN TRADE")
            return True
        else:
            return False
    else:
        time.sleep(5)
        return False


def select_My_Ether():
    #EnumSelected = 0
    #while EnumSelected <2:
    etherite = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/etherite.png', confidence = 0.95)
    if etherite != None:
        etherLoc = pyautogui.center(etherite)
        etherX, etherY = etherLoc
        print("etherLoc: ", etherLoc)
        pyautogui.click(etherX, etherY)
        #EnumSelected += 1
        time.sleep(1)
        if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/selectedEtherite.png', confidence = 0.95) != None:
            print("one ether slelected for sure")
            return True

def select_My_Deca():
    #EnumSelected = 0
    #while EnumSelected <2:
    deca = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/deca2.png', confidence = 0.95)
    if deca != None:
        deca = pyautogui.center(deca)
        decaX, decaY = deca
        print("deca: ", deca)
        pyautogui.click(decaX, decaY)
        #EnumSelected += 1
        time.sleep(1)
        if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/sDeca.png', confidence = 0.95) != None:
            print("one deca slelected for sure")
            return True


def select_My_Pixie():
    #PnumSelected = 0
    #while PnumSelected <2:
    pixie = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/pixie.png', confidence = 0.95)
    if pixie != None:
        pixieLoc = pyautogui.center(pixie)
        pixieX, pixieY = pixieLoc
        print("pixieLoc: ", pixieLoc)
        pyautogui.click(pixieX, pixieY)
        #PnumSelected += 1
        time.sleep(1)
        if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/selectedPixie.png', confidence = 0.95) != None:
            print("one pixie selected for sure")
            return True

def revised_confirm_that_the_Item_Selected_and_Press_Trade(numie):
    if numie == 111:
        littleHelper = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/little.png', confidence = 0.95)#
        platRogue = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/platRogue.png', confidence = 0.95)#
        demonSpawn = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/demon.png', confidence = 0.95)#
        holyAvenger = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/holy.png', confidence = 0.95)#
        vampiress = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/vampiress.png', confidence = 0.95)#
        if littleHelper != None or vampiress != None or demonSpawn != None or holyAvenger != None or platRogue != None:
            if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/tradeaccepted.png', confidence = 0.85) != None:
                tradeLoc = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/tradebutton.png', confidence = 0.95)
                if tradeLoc != None:
                    #print("the trade accepted, bride slected, and the trade button has been found")
                    tradeLoc = pyautogui.center(tradeLoc)
                    tradeX, tradeY = tradeLoc
                    #pyautogui.hotkey('shift', 'command', '3')
                    pyautogui.click(tradeX, tradeY)
                    print("trade is ready!")
                    time.sleep(4)
                    if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/trading?.png', confidence = 0.85) == None:
                        print("trade finished")
                        pyautogui.hotkey('enter')
                        pyautogui.typewrite('have a good day. you can message me again after one minute if you want to trade again.')
                        pyautogui.hotkey('enter')
                        #stopRecord()
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                print("bride was found but trade accepted / button ready not found")
                return False
        else:
            return False
            
    if numie == 211:
        #holyAvenger = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/holy.png', confidence = 0.95)#
        #littleHelper = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/little.png', confidence = 0.95)#        
        zombieNurse = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/zombie.png', confidence = 0.95)#
        stanleyBunny = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/bunny.png', confidence = 0.95)#
        ghostHuntress = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/ghost2.png', confidence = 0.95)
        jackRipper = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/jack.png', confidence = 0.95)
        #vampiress = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/vampiress.png', confidence = 0.95)#
        frank = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/frank.png', confidence = 0.95)
        
        if frank != None or stanleyBunny != None or ghostHuntress != None or jackRipper != None or zombieNurse != None: # or littleHelper != None: 
            if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/tradeaccepted.png', confidence = 0.85) != None:
                tradeLoc = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/tradebutton.png', confidence = 0.95)
                if tradeLoc != None:
                    #print("the trade accepted, bride slected, and the trade button has been found")
                    tradeLoc = pyautogui.center(tradeLoc)
                    tradeX, tradeY = tradeLoc
                    #pyautogui.hotkey('shift', 'command', '3')
                    pyautogui.click(tradeX, tradeY)
                    print("trade is ready!")
                    time.sleep(4)
                    if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/trading?.png', confidence = 0.85) == None:
                        print("trade finished")
                        pyautogui.hotkey('enter')
                        pyautogui.typewrite('have a good day. you can message me again after one minute if you want to trade again.')
                        pyautogui.hotkey('enter')
                        #stopRecord()
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                print("bride was found but trade accepted / button ready not found")
                return False
        else:
            return False

    '''
    if numie == 222:
        if vampiress != None:
            if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/tradeaccepted.png', confidence = 0.85) != None:
                tradeLoc = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/tradebutton.png', confidence = 0.95)
                if tradeLoc != None:
                    #print("the trade accepted, bride slected, and the trade button has been found")
                    tradeLoc = pyautogui.center(tradeLoc)
                    tradeX, tradeY = tradeLoc
                    #pyautogui.hotkey('shift', 'command', '3')
                    pyautogui.click(tradeX, tradeY)
                    print("trade is ready!")
                    time.sleep(4)
                    if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/trading?.png', confidence = 0.85) == None:
                        print("trade finished")
                        pyautogui.hotkey('enter')
                        pyautogui.typewrite('have a good day.')
                        pyautogui.hotkey('enter')
                        #stopRecord()
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                print("bride was found but trade accepted / button ready not found")
                return False
        else:
            return False
    '''

    if numie == 222:
        #print('yo')
        bride = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/bride.png', confidence = 0.95)
        #polter = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/polter.png', confidence = 0.95)
        #vampire = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/vampire.png', confidence = 0.95)
        #imp = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/imp.png', confidence = 0.95)
        #skelly = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/skelly.png', confidence = 0.95)
        if bride != None: #or polter != None skelly != None or imp != None or vampire != None or
            #print('stage one')
            if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/tradeaccepted.png', confidence = 0.85) != None:
                #print('stage 2')
                tradeLoc = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/tradebutton.png', confidence = 0.95)
                if tradeLoc != None:
                    #print("the trade accepted, bride slected, and the trade button has been found")
                    tradeLoc = pyautogui.center(tradeLoc)
                    tradeX, tradeY = tradeLoc
                    #pyautogui.hotkey('shift', 'command', '3')
                    pyautogui.click(tradeX, tradeY)
                    print("trade is ready!")
                    time.sleep(4)
                    if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/trading?.png', confidence = 0.85) == None:
                        print("trade finished")
                        pyautogui.hotkey('enter')
                        pyautogui.typewrite('have a good day. you can message me again after one minute if you want to trade again.')
                        pyautogui.hotkey('enter')
                        #stopRecord()
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                print("bride was found but trade accepted / button ready not found")
                return False
        else:
            return False

def confirm_that_the_Item_Selected_and_Press_Trade():
    #frank = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/frank.png', confidence = 0.95)
    bride = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/bride.png', confidence = 0.95)
    polter = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/polter.png', confidence = 0.95)
    #vampire = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/vampire.png', confidence = 0.95)
    #ghost = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/ghost2.png', confidence = 0.95)
    #skelly = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/skelly.png', confidence = 0.95)
    imp = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/imp.png', confidence = 0.95)
    if bride != None or polter != None or imp != None: # or vampire != None:  
        print("bride selected once!")
        if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/tradeaccepted.png', confidence = 0.85) != None:
            tradeLoc = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/tradebutton.png', confidence = 0.95)
            if tradeLoc != None:
                #print("the trade accepted, bride slected, and the trade button has been found")
                tradeLoc = pyautogui.center(tradeLoc)
                tradeX, tradeY = tradeLoc
                #pyautogui.hotkey('shift', 'command', '3')
                pyautogui.click(tradeX, tradeY)
                print("trade is ready!")
                time.sleep(4)
                if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/trading?.png', confidence = 0.85) == None:
                    print("trade finished")
                    pyautogui.hotkey('enter')
                    pyautogui.typewrite('have a good day. you can message me again after one minute if you want to trade again.')
                    pyautogui.hotkey('enter')
                    #stopRecord()
                    return True
                else:
                    return False
            else:
                return False
        else:
            print("bride was found but trade accepted / button ready not found")
            return False
    else:
        return False


def what_item_selected():
    platRogue = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/platRogue.png', confidence = 0.95)#
    demonSpawn = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/demon.png', confidence = 0.95)#
    
    littleHelper = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/little.png', confidence = 0.95)#
    holyAvenger = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/holy.png', confidence = 0.95)#
    zombieNurse = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/zombie.png', confidence = 0.95)#
    stanleyBunny = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/bunny.png', confidence = 0.95)#
    ghostHuntress = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/ghost2.png', confidence = 0.95)
    jackRipper = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/jack.png', confidence = 0.95)#
    frank = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/frank.png', confidence = 0.95)
        
    vampiress = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/vampiress.png', confidence = 0.95)#

    bride = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/bride.png', confidence = 0.95)
    #polter = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/polter.png', confidence = 0.95)
    #vampire = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/vampire.png', confidence = 0.95)
    #imp = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/imp.png', confidence = 0.95)
    #skelly = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/skelly.png', confidence = 0.95)
    
    if vampiress != None or demonSpawn != None or littleHelper != None or platRogue != None or holyAvenger != None:
        return 111
    
    if frank != None or stanleyBunny != None or ghostHuntress != None or jackRipper != None or zombieNurse != None: # or littleHelper != None:
        return 211

    if bride != None: 
        return 222

    #if vampire != None or bride != None or imp != None or skelly != None:  # or vampire != None or bride != None: or polter != None
        #return 222
    
    else:
        return 000
        
 

def skinTradeP():
    pyautogui.typewrite('r')
    time.sleep(3)
    goKeys()
    time.sleep(10)
    #while acceptTradeRequest() != True:
        #acceptTradeRequest()
        #print("still trying to accept request")
    
    count = 0
    loop = True
    while loop:
        trading = acceptTradeRequest()
        print('trading?: ', trading)
        if trading == True:
            loop = False
            #startRecord() #important
            print("request accepted, started recording, and about to select ethers")
        if trading == False:
            count+=1
            #if count % 4 == 0:
                #pyautogui.hotkey("enter")
                #pyautogui.typewrite("you have not requested to trade with me yet.")
                #pyautogui.hotkey('enter')
            #print("count: ", count)
            if count >= 15: #50 seconds wait for request
                #print("came.")
                loop = False
                pyautogui.hotkey("enter")
                pyautogui.typewrite("you have not requested to trade with me. You can message me in a few minutes to try again.")
                pyautogui.hotkey('enter')
                reset2()
                return
                #This is where I have to come up with a RESET and get me back to vault
        print("still trying to accept request")
    print("about to select")
    time.sleep(1) 

    
    for i in range(0,2):
        while select_My_Pixie() != True:
            select_My_Pixie()

    time.sleep(2)

    count2 = 0
    loop1 = True
    while loop1:
        done = confirm_that_the_Item_Selected_and_Press_Trade()
        print('done: ', done)
        if done == True:
            client = Client("ACf3d6e998fce70398ba2e11c55f99d441", "0759088a22e0e6e81ff17a0729ef1348")
            client.messages.create(to="+17326103038", 
                                from_="+12513062877", 
                                body="Pixie trade is done!")
            loop1 = False
            print("trade done")
            #stopRecord()
            reset2()
            if depositP() == False:
                return False
            if replenish() == False:
                return False
            return
        if done == False:
            count+=1
            #pyautogui.hotkey('enter')
            #pyautogui.typewrite("You have not selected the item i want and confirmed the trade.")
           #pyautogui.hotkey('enter')
            time.sleep(5)
            if count >= 15: #50 seconds wait for items to be selected
                loop1 = False
                pyautogui.hotkey("enter")
                pyautogui.typewrite("you have not selected the item i want. goodbye")
                pyautogui.hotkey('enter')
                #stopRecord()
                #This is where I have to come up with a RESET and get me back to vault
        print("still trying to confirm trade")

    reset2()

def revised_skinTradeP():
    pyautogui.typewrite('r')
    time.sleep(3)
    goKeys()
    time.sleep(10)
    #while acceptTradeRequest() != True:
        #acceptTradeRequest()
        #print("still trying to accept request")
    
    count = 0
    loop = True
    while loop:
        checkwhisperNotReady()
        trading = acceptTradeRequest()
        print('trading?: ', trading)
        if trading == True:
            loop = False
            #startRecord() #important
            print("request accepted, started recording, and about to select pixies")
        if trading == False:
            count+=1
            #if count % 4 == 0:
                #pyautogui.hotkey("enter")
                #pyautogui.typewrite("you have not requested to trade with me yet.")
                #pyautogui.hotkey('enter')
            #print("count: ", count)
            if count >= 15: #50 seconds wait for request
                #print("came.")
                loop = False
                pyautogui.hotkey("enter")
                pyautogui.typewrite("you have not requested to trade with me. You can message me in a few minutes to try again.")
                pyautogui.hotkey('enter')
                reset2()
                return
                #This is where I have to come up with a RESET and get me back to vault
        print("still trying to accept request")
    print("about to select")
    
    #time.sleep(5)  #wait for item to be selected
    
    
    loop = True
    x=0
    while loop:
        checkwhisperNotReady()
        numie = what_item_selected()
        if numie == 000:
            x += 1
            time.sleep(1)
            #print('no skin selected')
        else:
            loop = False
            print('skin is selected')
        if x == 30:
            pyautogui.hotkey("enter")
            pyautogui.typewrite("you have not selected the skin. You can message me in a few minutes to try again.")
            pyautogui.hotkey('enter')
            reset2()
            loop = False
            return
    
    
    #numie = what_item_selected()       
    print('numie: ', numie)
    list1 = list(str(numie))
    numPixies = int(list1[1])
    print('numpixies: ', numPixies)

    for i in range(0,numPixies):
        while select_My_Pixie() != True:
            select_My_Pixie()

    time.sleep(2)

    count2 = 0
    loop1 = True
    while loop1:
        checkwhisperNotReady()
        done = revised_confirm_that_the_Item_Selected_and_Press_Trade(numie)
        print('done: ', done)
        if done == True:
            client = Client("ACf3d6e998fce70398ba2e11c55f99d441", "0759088a22e0e6e81ff17a0729ef1348")
            client.messages.create(to="+17326103038", 
                                from_="+12513062877", 
                                body="Pixie trade is done!")
            loop1 = False
            print("trade done")
            #stopRecord()  #important
            reset2()
            if depositP() == False:
                return False
            if replenish() == False:
                return False
            return
        if done == False:
            count+=1
            #pyautogui.hotkey('enter')
            #pyautogui.typewrite("You have not selected the item i want and confirmed the trade.")
           #pyautogui.hotkey('enter')
            time.sleep(5)
            if count >= 15: #50 seconds wait for items to be selected
                loop1 = False
                pyautogui.hotkey("enter")
                pyautogui.typewrite("you have not selected the item i want. goodbye")
                pyautogui.hotkey('enter')
                #stopRecord() #important
                #This is where I have to come up with a RESET and get me back to vault
        print("still trying to confirm trade")

    reset2()

def skinTradeD():
    pyautogui.typewrite('r')
    time.sleep(3)
    goKeys()
    time.sleep(10)
    #while acceptTradeRequest() != True:
        #acceptTradeRequest()
        #print("still trying to accept request")
    
    count = 0
    loop = True
    while loop:
        trading = acceptTradeRequest()
        print('trading?: ', trading)
        if trading == True:
            loop = False
            #startRecord()  #important
            print("request accepted, recording started, and about to select ethers")
        if trading == False:
            count+=1
            #if count % 4 == 0:
                #pyautogui.hotkey("enter")
                #pyautogui.typewrite("you have not requested to trade with me yet.")
                #pyautogui.hotkey('enter')
            #print("count: ", count)
            if count >= 15:
                #print("came.")
                loop = False
                pyautogui.hotkey("enter")
                pyautogui.typewrite("you have not requested to trade with me. You can message me in a few minutes to try again.")
                pyautogui.hotkey('enter')
                reset2()
                return
                #This is where I have to come up with a RESET and get me back to vault
        print("still trying to accept request")
    print("about to select")
    time.sleep(1)

    for i in range(0,3):
        while select_My_Deca() != True:
            select_My_Deca()

    time.sleep(2)

    count2 = 0
    loop1 = True
    while loop1:
        done = confirm_that_the_Item_Selected_and_Press_Trade()
        print('done: ', done)
        if done == True:
            client = Client("ACf3d6e998fce70398ba2e11c55f99d441", "0759088a22e0e6e81ff17a0729ef1348")
            client.messages.create(to="+17326103038", 
                                from_="+12513062877", 
                                body="Deca Trade has been Done!")
            loop1 = False
            print("trade done")
            #stopRecord() #important
            reset2()
            if depositD() == False:
                return False
            if replenish() == False:
                return False
            return
        if done == False:
            count+=1
            #pyautogui.hotkey('enter')
            #pyautogui.typewrite("You have not selected the item i want and confirmed the trade.")
            #pyautogui.hotkey('enter')
            time.sleep(5)
            if count >= 15:
                loop1 = False
                pyautogui.hotkey("enter")
                pyautogui.typewrite("you have not selected the item i want. goodbye")
                pyautogui.hotkey('enter')
                #stopRecord() #important
                #This is where I have to come up with a RESET and get me back to vault
        print("still trying to confirm trade")

    reset2()

def revised_skinTradeD():
    pyautogui.typewrite('r')
    time.sleep(3)
    goKeys()
    time.sleep(10)
    #while acceptTradeRequest() != True:
        #acceptTradeRequest()
        #print("still trying to accept request")
    
    count = 0
    loop = True
    while loop:
        checkwhisperNotReady()
        trading = acceptTradeRequest()
        print('trading?: ', trading)
        if trading == True:
            loop = False
            #startRecord() #important
            print("request accepted, started recording, and about to select decas")
        if trading == False:
            count+=1
            #if count % 4 == 0:
                #pyautogui.hotkey("enter")
                #pyautogui.typewrite("you have not requested to trade with me yet.")
                #pyautogui.hotkey('enter')
            #print("count: ", count)
            if count >= 15: #50 seconds wait for request
                #print("came.")
                loop = False
                pyautogui.hotkey("enter")
                pyautogui.typewrite("you have not requested to trade with me. You can message me in a few minutes to try again.")
                pyautogui.hotkey('enter')
                reset2()
                return
                #This is where I have to come up with a RESET and get me back to vault
        print("still trying to accept request")
    print("about to select")
    
    #time.sleep(5)  #wait for item to be selected
    loop = True
    x=0
    while loop:
        checkwhisperNotReady()
        numie = what_item_selected()
        if numie == 000:
            x += 1
            time.sleep(1)
            #print('no skin selected')
        else:
            loop = False
            print('skin is selected')
        if x == 30:
            pyautogui.hotkey("enter")
            pyautogui.typewrite("you have not selected the skin. You can message me in a few minutes to try again.")
            pyautogui.hotkey('enter')
            reset2()
            loop = False
            return
    #numie = what_item_selected()
    print('numie: ', numie)
    list1 = list(str(numie))
    numdecas = int(list1[0])
    print('numdecas: ', numdecas)

    for i in range(0,numdecas):
        while select_My_Deca() != True:
            select_My_Deca()

    time.sleep(2)

    count2 = 0
    loop1 = True
    while loop1:
        checkwhisperNotReady()
        done = revised_confirm_that_the_Item_Selected_and_Press_Trade(numie)
        print('done: ', done)
        if done == True:
            client = Client("ACf3d6e998fce70398ba2e11c55f99d441", "0759088a22e0e6e81ff17a0729ef1348")
            client.messages.create(to="+17326103038", 
                                from_="+12513062877", 
                                body="Deca trade is done!")
            loop1 = False
            print("trade done")
            #stopRecord() #important
            reset2()
            if depositD() == False:
                return False
            if replenish() == False:
                return False
            return
        if done == False:
            count+=1
            #pyautogui.hotkey('enter')
            #pyautogui.typewrite("You have not selected the item i want and confirmed the trade.")
           #pyautogui.hotkey('enter')
            time.sleep(5)
            if count >= 15: #50 seconds wait for items to be selected
                loop1 = False
                pyautogui.hotkey("enter")
                pyautogui.typewrite("you have not selected the item i want. goodbye")
                pyautogui.hotkey('enter')
                #stopRecord() #important
                #This is where I have to come up with a RESET and get me back to vault
        print("still trying to confirm trade")

    reset2()


def skinTradeE():
    pyautogui.typewrite('r')
    time.sleep(3)
    goKeys()
    #while acceptTradeRequest() != True:
        #acceptTradeRequest()
        #print("still trying to accept request")
    time.sleep(10)
    count = 0
    loop = True
    while loop:
        trading = acceptTradeRequest()
        print('trading?: ', trading)
        if trading == True:
            loop = False
            #startRecord() #important
            print("request accepted, recording started, and about to select ethers")
        if trading == False:
            count+=1
            #if count % 4 == 0:
                #pyautogui.hotkey("enter")
                #pyautogui.typewrite("you have not requested to trade with me yet.")
                #pyautogui.hotkey('enter')
            #print("count: ", count)
            if count >= 15:
                loop = False
                pyautogui.hotkey("enter")
                pyautogui.typewrite("you have not requested to trade with me. You can message me in a few minutes to try again.")
                pyautogui.hotkey('enter')
                reset2()
                return
                #This is where I have to come up with a RESET and get me back to vault
        print("still trying to accept request")

    time.sleep(1)
    print("about to select")
    for i in range(0,2):
        while select_My_Ether() != True:
            select_My_Ether()


    time.sleep(2)

    count2 = 0
    loop1 = True
    while loop1:
        done = confirm_that_the_Item_Selected_and_Press_Trade()
        print('done: ', done)
        if done == True:
            client = Client("ACf3d6e998fce70398ba2e11c55f99d441", "0759088a22e0e6e81ff17a0729ef1348")
            client.messages.create(to="+17326103038", 
                                from_="+12513062877", 
                                body="etherite trade has been done!")
            loop1 = False
            print("trade done")
            #stopRecord() #important
            reset2()
            if depositE() == False:
                return False
            if replenish() == False:
                return False
            return
        if done == False:
            count+=1
            #pyautogui.hotkey('enter')
            #pyautogui.typewrite("You have not selected the item i want and confirmed the trade.")
            #pyautogui.hotkey('enter')
           
            time.sleep(5)
            if count >= 15:
                loop1 = False
                pyautogui.hotkey("enter")
                pyautogui.typewrite("you have not selected the item i want. goodbye")
                pyautogui.hotkey('enter')
                #stopRecord() #important
                #This is where I have to come up with a RESET and get me back to vault
        print("still trying to confirm trade")

    reset2()

def revised_skinTradeE():
    pyautogui.typewrite('r')
    time.sleep(3)
    goKeys()
    time.sleep(10)
    #while acceptTradeRequest() != True:
        #acceptTradeRequest()
        #print("still trying to accept request")
    
    count = 0
    loop = True
    while loop:
        checkwhisperNotReady()
        trading = acceptTradeRequest()
        print('trading?: ', trading)
        if trading == True:
            loop = False
            #startRecord() #important
            print("request accepted, started recording, and about to select ethers")
        if trading == False:
            count+=1
            #if count % 4 == 0:
                #pyautogui.hotkey("enter")
                #pyautogui.typewrite("you have not requested to trade with me yet.")
                #pyautogui.hotkey('enter')
            #print("count: ", count)
            if count >= 15: #50 seconds wait for request
                #print("came.")
                loop = False
                pyautogui.hotkey("enter")
                pyautogui.typewrite("you have not requested to trade with me. You can message me in a few minutes to try again.")
                pyautogui.hotkey('enter')
                reset2()
                return
                #This is where I have to come up with a RESET and get me back to vault
        print("still trying to accept request")
    print("about to select")
    
    #time.sleep(5)  #wait for item to be selected
    loop = True
    x=0
    while loop:
        checkwhisperNotReady()
        numie = what_item_selected()
        if numie == 000:
            x += 1
            time.sleep(1)
            #print('no skin selected')
        else:
            loop = False
            print('skin is selected')
        if x == 30:
            pyautogui.hotkey("enter")
            pyautogui.typewrite("you have not selected the skin. You can message me in a few minutes to try again.")
            pyautogui.hotkey('enter')
            reset2()
            loop = False
            return
    #numie = what_item_selected()
    print('numie: ', numie)
    list1 = list(str(numie))
    numEthers = int(list1[2])
    print('numEthers: ', numEthers)

    for i in range(0,numEthers):
        while select_My_Ether() != True:
            select_My_Ether()

    time.sleep(2)

    count2 = 0
    loop1 = True
    while loop1:
        checkwhisperNotReady()
        done = revised_confirm_that_the_Item_Selected_and_Press_Trade(numie)
        print('done: ', done)
        if done == True:
            client = Client("ACf3d6e998fce70398ba2e11c55f99d441", "0759088a22e0e6e81ff17a0729ef1348")
            client.messages.create(to="+17326103038", 
                                from_="+12513062877", 
                                body="Ether trade is done!")
            loop1 = False
            print("trade done")
            #stopRecord() #important
            reset2()
            if depositE() == False:
                return False
            if replenish() == False:
                return False
            return
        if done == False:
            count+=1
            #pyautogui.hotkey('enter')
            #pyautogui.typewrite("You have not selected the item i want and confirmed the trade.")
           #pyautogui.hotkey('enter')
            time.sleep(5)
            if count >= 15: #50 seconds wait for items to be selected
                loop1 = False
                pyautogui.hotkey("enter")
                pyautogui.typewrite("you have not selected the item i want. goodbye")
                pyautogui.hotkey('enter')
                #stopRecord() #important
                #This is where I have to come up with a RESET and get me back to vault
        print("still trying to confirm trade")

    reset2()


def returnToVault():
    x=0
    y=0
    #checkwhisperNotReady()
    while True:
        record = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/vault3.png', confidence = 0.75)
        if record != None:
            record = pyautogui.center(record)
            recordX, recordY = record
            time.sleep(1)
            pyautogui.click(recordX, recordY)
            pyautogui.hotkey('space')
            time.sleep(2)
            checkwhisperNotReady()
            time.sleep(2)
            pyautogui.hotkey('shift')
            pyautogui.hotkey('shift')
            pyautogui.hotkey('shift')
            time.sleep(8)
            pyautogui.typewrite('z')
            time.sleep(0.3)
            pyautogui.keyDown('w')
            time.sleep(0.03) 
            pyautogui.keyUp('w')

            return
        else: 
            print("vault not found")
            x+=1
            y+=1
        if x == 3:
            pyautogui.keyDown('e')
            time.sleep(0.25)
            pyautogui.keyUp('e')
            checkwhisperNotReady()
            x=0
        if y == 500: 
            checkwhisperNotReady()
            screenie()
            client = Client("ACf3d6e998fce70398ba2e11c55f99d441", "0759088a22e0e6e81ff17a0729ef1348")
            client.messages.create(to="+17326103038", 
                                from_="+12513062877", 
                                body="Vault has not been found in a while. Doing a full reset")
            y=0
            if fullreset() == False:
                return False
            else:
                return
            #do this now
            #return False

            '''
            time.sleep(600) #how long a dc lasts
            pyautogui.click(142,448)
            pyautogui.hotkey('command', 'r')
            time.sleep(30)
            play = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/play.png', confidence = 0.65)
            if play != None:
                play = pyautogui.center(play)
                playX, playY = play
                pyautogui.click(playX, playY)
                time.sleep(2)
            play2 = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/play2.png', confidence = 0.65)
            if play2 != None:
                play2 = pyautogui.center(play2)
                pX, pY = play2
                pyautogui.click(pX, pY)
                time.sleep(2)
                print('where am i now?')
                #returnToVault()
                #print('now it should finish')
            '''


def returnToVault2():
    x=0
    y=0
    #checkwhisperNotReady()
    while True:
        record = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/vault3.png', confidence = 0.75)
        if record != None:
            record = pyautogui.center(record)
            recordX, recordY = record
            time.sleep(1)
            pyautogui.click(recordX, recordY)
            pyautogui.hotkey('space')
            time.sleep(5)
            pyautogui.hotkey('shift')
            pyautogui.hotkey('shift')
            pyautogui.hotkey('shift')
            time.sleep(5)
            pyautogui.typewrite('z')
            time.sleep(0.3)
            pyautogui.keyDown('w')
            time.sleep(0.03)
            pyautogui.keyUp('w')
            
            return
        else: 
            print("vault not found")
            x+=1
            y+=1
        if x == 3:
            pyautogui.keyDown('e')
            time.sleep(0.25)
            pyautogui.keyUp('e')
            x=0
        if y == 500: 
            checkwhisperNotReady()
            screenie()
            client = Client("ACf3d6e998fce70398ba2e11c55f99d441", "0759088a22e0e6e81ff17a0729ef1348")
            client.messages.create(to="+17326103038", 
                                from_="+12513062877", 
                                body="Vault has not been found even after a fullreset. program will stop now.")
            y=0
            return False
            #do this now
            #return False

def refreshwText():
    time.sleep(1)
    pyautogui.click(223,40) #tab 1
    time.sleep(1)
    pyautogui.click(441,40) #tab 2
    time.sleep(1)
    pyautogui.click(518,416) #publish offers button
    time.sleep(3)
    pyautogui.click(1224,26)#click on tab 6
    pyautogui.hotkey('command', 'r')
    time.sleep(3)
    pyautogui.click(800,400) #middle of screen 
    pyautogui.keyDown('down')
    time.sleep(2)
    pyautogui.keyUp('down')
    time.sleep(1)
    if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/3D4Skelly.png') != None:
        client = Client("ACf3d6e998fce70398ba2e11c55f99d441", "0759088a22e0e6e81ff17a0729ef1348")
        client.messages.create(to="+17326103038", 
                                from_="+12513062877", 
                                body="Someone is paying 3 decas for skelly")
    time.sleep(1)
    pyautogui.click(223,40) #tab one
    time.sleep(1)
    pyautogui.click(350,700) #middle of screen 

def refresh():
    time.sleep(1)
    offers = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/offersTab.png', confidence = 0.45)
    if offers != None:
        offers = pyautogui.center(offers)
        oX, oY = offers
        time.sleep(1)
        pyautogui.click(oX, oY)    
    time.sleep(1)
    publish = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/saveChanges.png', confidence = 0.45)
    if publish != None:
        p = pyautogui.center(publish)
        pX, pY = p
        time.sleep(1)
        pyautogui.click(pX, pY)    
    time.sleep(3)
    realm = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/realmTab.png', confidence = 0.45)
    if realm != None:
        realm = pyautogui.center(realm)
        rX, rY = realm
        time.sleep(1)
        pyautogui.click(rX, rY) 
    time.sleep(1)
    pyautogui.click(350,700) #middle of screen

    #pyautogui.click(1224,26)#click on tab 6
    #pyautogui.hotkey('command', 'r')
    #time.sleep(3)
    #pyautogui.click(800,400) #middle of screen 
    #pyautogui.keyDown('down')
    #time.sleep(2)
    #pyautogui.keyUp('down')
    #time.sleep(1)
    #if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/3D4Skelly.png') != None:
        #client = Client("ACf3d6e998fce70398ba2e11c55f99d441", "0759088a22e0e6e81ff17a0729ef1348")
        #client.messages.create(to="+17326103038", 
                                #from_="+12513062877", 
                                #body="Someone is paying 3 decas for skelly")
    #time.sleep(1)
    #pyautogui.click(223,40) #tab one
    #time.sleep(1)

def checkFCW():
    pyautogui.click(660,40) #tab 3
    pyautogui.click(800,400) #mid of page
    pyautogui.hotkey('command', 'r')
    time.sleep(3)
    if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/minute.png') != None:
        print("FCW found")
        client = Client("ACf3d6e998fce70398ba2e11c55f99d441", "0759088a22e0e6e81ff17a0729ef1348")
        client.messages.create(to="+17326103038", 
                            from_="+12513062877", 
                            body="FCW is online!!")
    else: 
        print("fcw not found")


def Communicator():
    pyautogui.click(350,700)
    pyautogui.hotkey('tab')
    time.sleep(1)
    pyautogui.typewrite("hi. i am a bot coded by eddienew that buys skins that are shown on my realmeye. that is all i can do.")
    pyautogui.hotkey('enter')
    time.sleep(1)
    pyautogui.hotkey('tab')
    time.sleep(1)
    pyautogui.typewrite("type anything if you have a skin that you want to sell to me. i will only pay what is shown on realmeye.")
    pyautogui.hotkey('enter')
    time.sleep(1)
    
    
    loop10 = True
    z = 0
    while loop10:
        if pyautogui.pixelMatchesColor(350, 700, (0, 92, 97)) == True or pyautogui.pixelMatchesColor(350, 680, (0, 92, 97)) == True:
            loop10 = False
        else:
            z+=1
            time.sleep(5)
            if z > 4:
                return False
    '''
    time.sleep(1)
    pyautogui.hotkey('tab')
    pyautogui.typewrite("ok. also, i will only pay what is shown on my realmeye offer.")
    pyautogui.hotkey('enter')
    time.sleep(1)
    pyautogui.hotkey('tab')
    pyautogui.typewrite("if you would like to negotiate, or have any other questions, send me a realmeye message and i will see it later.")
    pyautogui.hotkey('enter')
    time.sleep(1)
    pyautogui.hotkey('tab')
    time.sleep(1)
    pyautogui.hotkey('tab')
    time.sleep(1)
    pyautogui.typewrite("type anything if you have a skin that you want to sell to me.")
    pyautogui.hotkey('enter')
    time.sleep(1)
    loop101 = True
    y = 0
    while loop101:
        if pyautogui.pixelMatchesColor(350, 700, (0, 92, 97)) == True or pyautogui.pixelMatchesColor(350, 680, (0, 92, 97)) == True:
            loop101 = False
        else:
            y+=1
            time.sleep(5)
            if y > 5:
                return False
    '''
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
    loopA = True
    '''
    a = 0
    while loopA:
        if pyautogui.pixelMatchesColor(350, 700, (0, 92, 97)) == True or pyautogui.pixelMatchesColor(350, 680, (0, 92, 97)) == True:
            loopA= False
        else:
            a+=1
            time.sleep(5)
            if a > 5:
                return False
    '''


def Communicator2():
    pyautogui.click(350,700)
    counter = 0
    found = True
    while found:
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
        time.sleep(1)
        if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/intro.png', confidence = 0.75) != None:
            found = False
        else:
            time.sleep(3)
            counter += 1
            if counter == 5:
                return False


    pyautogui.hotkey('tab')
    time.sleep(2)
    pyautogui.typewrite("i will only pay what I posted on realmeye. i am sorry i cannot answer any questions or be negotiable.")
    pyautogui.hotkey('enter')

    time.sleep(19)
    count = 0
    loop = True
    while loop:
        if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/YYY.png', confidence = 0.65) != None: 
            
            counter = 0
            found = True
            while found:
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
                time.sleep(1)
                if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/payment.png', confidence = 0.65) != None:
                    found = False
                else:
                    time.sleep(3)
                    counter += 1
                    if counter == 5:
                        return False

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

        elif pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/NNN.png', confidence = 0.65) != None: 
            pyautogui.hotkey('tab')
            time.sleep(1)
            pyautogui.typewrite("ok. have a good day. sorry i did not trade with you.")
            pyautogui.hotkey('enter')
            time.sleep(5)
            return False

        else:
            if count % 3 == 0:
                pyautogui.hotkey('tab')
                pyautogui.typewrite("you have not chosen a response yet.")
                pyautogui.hotkey('enter')
                time.sleep(7)
            count+=1
            print("count: ", count)
            if count > 7: #20 + 15 = 35 seconds wait for response
                pyautogui.hotkey('tab')
                pyautogui.typewrite("you have not chosen a response. message me again if you still want to trade. goodbye.")
                pyautogui.hotkey('enter')
                loop = False
                time.sleep(10)
                return False
        print("still in loop checking for response")





def checkResponse():
    if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/EEE.png', confidence = 0.85) != None: #or pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/uee.png', confidence = 0.85) != None:
        counter = 0
        found = True
        while found:
            pyautogui.hotkey('tab')
            pyautogui.typewrite("ok. come asiasoutheast keys. you have 40 seconds. you must request to trade with me. ")
            pyautogui.hotkey('enter')
            time.sleep(1)
            if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/comekeys.png', confidence = 0.65) != None:
                found = False
            else:
                time.sleep(3)
                counter += 1
                if counter == 5:
                    return 'xx'

        time.sleep(1)
        pyautogui.hotkey('tab')
        pyautogui.typewrite("make sure you have the items ready in your inventory and select it. i am recording. do not try to scam me.")
        pyautogui.hotkey('enter')
        time.sleep(1)
        print('etherites are wanted')
        return "e"
    elif pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/DDD.png', confidence = 0.85) != None: # or pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/udd.png', confidence = 0.85) != None:
        counter = 0
        found = True
        while found:
            pyautogui.hotkey('tab')
            pyautogui.typewrite("ok. come asiasoutheast keys. you have 40 seconds. you must request to trade with me. ")
            pyautogui.hotkey('enter')
            time.sleep(1)
            if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/comekeys.png', confidence = 0.65) != None:
                found = False
            else:
                time.sleep(3)
                counter += 1
                if counter == 5:
                    return 'xx'

        time.sleep(1)
        pyautogui.hotkey('tab')
        pyautogui.typewrite("make sure you have the items ready in your inventory and select it. i am recording. do not try to scam me.")
        pyautogui.hotkey('enter')
        time.sleep(1)
        print('decas are wanted')
        return "d"
    elif pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/PPP.png', confidence = 0.85) != None: # or pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/upp.png', confidence = 0.85) != None:
        counter = 0
        found = True
        while found:
            pyautogui.hotkey('tab')
            pyautogui.typewrite("ok. come asiasoutheast keys. you have 40 seconds. you must request to trade with me. ")
            pyautogui.hotkey('enter')
            time.sleep(1)
            if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/comekeys.png', confidence = 0.65) != None:
                found = False
            else:
                time.sleep(3)
                counter += 1
                if counter == 5:
                    return 'xx'

        time.sleep(1)
        pyautogui.hotkey('tab')
        pyautogui.typewrite("make sure you have the items ready in your inventory and select it. i am recording. do not try to scam me.")
        pyautogui.hotkey('enter')   
        time.sleep(1)     
        print('pixies are wanted')
        return "p"
    elif pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/XXX.png', confidence = 0.85) != None: # or pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/uxx.png', confidence = 0.85) != None:
        pyautogui.hotkey('tab')
        pyautogui.typewrite("ok. have a good day.")
        pyautogui.hotkey('enter')
        time.sleep(1)
        print('nothing is wanted')
        #stopRecord()
        return "x"
    else:
        return "n/a"
        
def checkWhisper(x):
    if x < 29: #one less than the one in main
        #k = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/whisper2.png', confidence=0.9)
        #if k != None:
        pyautogui.click(350,680)
        time.sleep(2) #?
        if pyautogui.pixelMatchesColor(350, 700, (0, 92, 97)) == True or pyautogui.pixelMatchesColor(350, 680, (0, 92, 97)) == True:
            print("whisper found")
            #client = Client("ACf3d6e998fce70398ba2e11c55f99d441", "0759088a22e0e6e81ff17a0729ef1348")
            #client.messages.create(to="+17326103038", 
            #                    from_="+12513062877", 
            #                    body="Someone wants to sell you a skin!")
            startRecord() #!
            #time.sleep(15)

            #pyautogui.keyDown('shift')
           # pyautogui.keyDown('command')
            #pyautogui.keyDown('3')    
           # pyautogui.keyUp('shift')
           # pyautogui.keyUp('command')
           # pyautogui.keyUp('3')
           # sendAmanda()

            
            
           
            if Communicator() == False:
                print("this should restart the program?")
                stopRecord() #!
                return #this should restart the program?
            time.sleep(24)
            

            count = 0
            loop = True
            while loop:
                pyautogui.click(350,700)
                result = checkResponse()
                pyautogui.click(340,700)
                pyautogui.click()
                print('result: ', result)
                if result == "e":
                    if revised_skinTradeE() == False:
                        stopRecord() #!
                        return False
                    else:
                        stopRecord() #!
                        #print('this should run@!!!')
                    loop = False

                if result == "d":
                    if revised_skinTradeD() == False:
                        stopRecord() #!
                        return False
                    else:
                        stopRecord() #!
                    loop = False

                if result == "p":
                    if revised_skinTradeP() == False:
                        stopRecord() #!
                        return False
                    else:
                        stopRecord() #!
                    loop = False

                if result == "x":
                    time.sleep(30) #to wait for the persons dm to go away
                    print("waiting for persons dm to go away")
                    stopRecord() #!
                    loop = False
                
                if result == "xx":
                    stopRecord() #!
                    loop = False
                    return

                if result == "n/a":
                    if count % 4 == 0:
                        pyautogui.hotkey('tab')
                        pyautogui.typewrite("you have not chosen a response yet.")
                        pyautogui.hotkey('enter')
                        time.sleep(7)
                    count+=1
                    if count > 9: #20 + 15 = 35 seconds wait for response
                        pyautogui.hotkey('tab')
                        pyautogui.typewrite("you have not chosen a response. message me again if you still want to trade. Goodbye.")
                        pyautogui.hotkey('enter')
                        time.sleep(10)
                        stopRecord() #!
                        loop = False
                print("still in loop checking for response")
        
        
                    
        else: 
            print("whisper not found")
            #now check isellskins whispers
            #pyautogui.click(641,27) #tab 4 (added)
            #checkWhisperSellingSkins(1) #(added)
            #pyautogui.click(230,40) #added
            #time.sleep(1) #added
            #pyautogui.click(230,40) #added
            #time.sleep(5)  # (added)
            time.sleep(8) #(deleted)
            x += 1
            print("x: ", x)

            if x > 5:
                if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/nexus.png', confidence = 0.85) == None: # or pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/upp.png', confidence = 0.85) != None:
                    if fullreset() == False:
                        return False
    else:
        print("this shoudl run?")
        #checkFCW()
        refresh()
        pyautogui.typewrite(['r'])
        time.sleep(5)
        if returnToVault() == False:
            return False
        """
        g = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/gray.png')
        f = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/FCW.png')
        if g != None or f!=None:
            client = Client("ACf3d6e998fce70398ba2e11c55f99d441", "0759088a22e0e6e81ff17a0729ef1348")
            client.messages.create(to="+17326103038", 
                            from_="+12513062877", 
                            body="GrayBeech/FCW is online!")
        """


def checkWhisperSellingSkins(x):
    if x < 24: #one less than the one in main
        #k = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/whisper2.png', confidence=0.9)
        #if k != None:
        pyautogui.click(350,680)
        time.sleep(2) #?
        if pyautogui.pixelMatchesColor(350, 700, (0, 92, 97)) == True or pyautogui.pixelMatchesColor(350, 680, (0, 92, 97)) == True:
            print("whisper found")
            client = Client("ACf3d6e998fce70398ba2e11c55f99d441", "0759088a22e0e6e81ff17a0729ef1348")
            client.messages.create(to="+17326103038", 
                                from_="+12513062877", 
                                body="Someone wants to buy your skin!")
            client = Client("ACf3d6e998fce70398ba2e11c55f99d441", "0759088a22e0e6e81ff17a0729ef1348")
            client.messages.create(to="+17326101207", 
                                from_="+12513062877", 
                                body="Someone wants to buy your skin!")
            
            pyautogui.hotkey('tab')
            time.sleep(1)
            pyautogui.typewrite("hey man whats up")
            pyautogui.hotkey('enter')

            time.sleep(12)
            screenie()
            #time.sleep(8)
            #sendAmanda()
            loop = True
            while loop:
                if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/DONE.png', confidence = 0.85) != None:
                    loop = False
                else:
                    time.sleep(5)
            
            #time.sleep(15)
            #pyautogui.keyDown('shift')
           # pyautogui.keyDown('command')
            #pyautogui.keyDown('3')    
           # pyautogui.keyUp('shift')
           # pyautogui.keyUp('command')
           # pyautogui.keyUp('3')
           # sendAmanda()

            
            ''' 
           
            if Communicator() == False:
                print("this should restart the program?")
                return #this should restart the program?
            time.sleep(17)

            count = 0
            loop = True
            while loop:
                result = checkResponse()
                print('result: ', result)
                if result == "e":
                    if revised_skinTradeE() == False:
                        return False
                    loop = False

                if result == "d":
                    if revised_skinTradeD() == False:
                        return False
                    loop = False

                if result == "p":
                    if revised_skinTradeP() == False:
                        return False
                    loop = False

                if result == "x":
                    time.sleep(30) #to wait for the persons dm to go away
                    print("waiting for persons dm to go away")
                    loop = False

                if result == "n/a":
                    pyautogui.hotkey('tab')
                    pyautogui.typewrite("you have not chosen a response yet.")
                    pyautogui.hotkey('enter')
                    time.sleep(10)
                    count+=1
                    if count > 3: #20 + 15 = 35 seconds wait for response
                        pyautogui.hotkey('tab')
                        pyautogui.typewrite("you have not chosen a response. Try again in a few minutes if you still want to trade. Goodbye.")
                        pyautogui.hotkey('enter')
                        #stopRecord()
                        loop = False
                print("still in loop checking for response")
        
            '''
                    
        else: 
            print("whisper not found")
            time.sleep(8) 
            #time.sleep(2) #(added)
            #pyautogui.click(230,40) # click on tab 1 (added)
            x += 1
            print("x: ", x)
            if x > 1:
                
                if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/life.png', confidence = 0.85) != None: # or pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/upp.png', confidence = 0.85) != None:
                        print('this should not run??')
                        time.sleep(120)
                        chrome = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/chrome.png', confidence = 0.75)
                        if chrome != None:
                            chrome = pyautogui.center(chrome)
                            cx, cy = chrome
                            pyautogui.click(cx, cy)
                            pyautogui.click(cx, cy)
                        loop = True
                        while loop:
                            if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/DONE.png', confidence = 0.85) != None:
                                loop = False
                            else:
                                time.sleep(5)
                        refresh()
                        time.sleep(1)
                        pyautogui.typewrite('r')
                        if returnToVault() == False:
                            return False
            if x > 5:
                if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/nexus.png', confidence = 0.85) == None: # or pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/upp.png', confidence = 0.85) != None:
                    print('this should not run')
                    if fullreset() == False:
                        return False
    else:
        print("this shoudl run?")
        #checkFCW()
        refresh()
        checkwhisperNotReady()
        pyautogui.typewrite(['r'])
        time.sleep(5)
        if returnToVault() == False:
            return False
        """
        g = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/gray.png')
        f = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/FCW.png')
        if g != None or f!=None:
            client = Client("ACf3d6e998fce70398ba2e11c55f99d441", "0759088a22e0e6e81ff17a0729ef1348")
            client.messages.create(to="+17326103038", 
                            from_="+12513062877", 
                            body="GrayBeech/FCW is online!")
        """
        
        

def main(): 
    pyautogui.typewrite('r')
    returnToVault()
    x=0
    loop = True
    while loop:
        if checkWhisper(x) == False:
            print("the Program has ended.")
            screenie()
            pyautogui.click(142,448)
            pyautogui.hotkey("command", "w")
            client = Client("ACf3d6e998fce70398ba2e11c55f99d441", "0759088a22e0e6e81ff17a0729ef1348")
            client.messages.create(to="+17326103038", 
                                from_="+12513062877", 
                                body="Program has ended due to insufficient items / full two chests of skins/ not being able to return to vault!")
            loop = False

        if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/movie.png', confidence = 0.85) != None: #or pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/uee.png', confidence = 0.85) != None:
            #screenie()
            print('curious if the internet shuts down')
        '''
        if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/movie.png', confidence = 0.85) != None: #or pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/uee.png', confidence = 0.85) != None:
            print("the Program has ended at 11:55.")
            pyautogui.keyDown('shift')
            pyautogui.keyDown('command')
            pyautogui.keyDown('3')
            pyautogui.keyUp('shift')
            pyautogui.keyUp('command')
            pyautogui.keyUp('3')
            time.sleep(5)
            pyautogui.click(142,448)
            pyautogui.hotkey("command", "w")
            loop = False
        '''
        x+=1
        if x == 30:
            x = 0

def main2(): 
    x=0
    loop = True
    while loop:
        if checkWhisperSellingSkins(x) == False:
            print("the Program has ended.")
            screenie()
            wpyautogui.click(142,448)
            pyautogui.hotkey("command", "w")
            client = Client("ACf3d6e998fce70398ba2e11c55f99d441", "0759088a22e0e6e81ff17a0729ef1348")
            client.messages.create(to="+17326103038", 
                                from_="+12513062877", 
                                body="Program has ended due to insufficient items / full two chests of skins/ not being able to return to vault!")
            loop = False
            
        x+=1
        if x == 25:
            x = 0

        


def main3():
    checkwhisperNotReady()

main()
#main2()
#main3()

''''
def skinTradePbad():

    pyautogui.typewrite('r')
    time.sleep(5)
    goKeys() 

    
    count = 0
    loop = True
    while loop:
        trading = acceptTradeRequest()
        print('trading?: ', trading)
        if trading == True:
            loop = False
            print("request accepted and about to select pixies")
        if trading == False:
            count+=1
            if count >= 5:
                loop = False
                #This is where I have to come up with a RESET and get me back to vault
        print("still trying to accept request")
        
    
    #while acceptTradeRequest() != True:
        #acceptTradeRequest()
       # print("still trying to accept request")

    time.sleep(1)

    for i in range(0,2):
        while select_My_Pixie() != True:
            select_My_Pixie()
            print("+1 pixie selected")

    time.sleep(2)

    while confirm_that_the_Item_Selected_and_Press_Trade() != True:
        confirm_that_the_Item_Selected_and_Press_Trade()
        print("still trying to confirm")
    
    reset()
'''