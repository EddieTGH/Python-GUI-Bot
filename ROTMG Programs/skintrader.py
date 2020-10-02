import pyautogui
import time
import cv2
from twilio.rest import Client

def acceptTradeRequest():
    request = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/accept.png', confidence = 0.85)
    if request != None:
        request = pyautogui.center(request)
        requestX, requestY = request
        pyautogui.click(requestX, requestY)
        time.sleep(2)
        if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/trading?.png', confidence = 0.85) != None:
            return True




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
            return True


def confirm_that_the_Item_Selected_and_Press_Trade():
    bride = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/bride.png', confidence = 0.95)
    huntsman = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/huntsman.png', confidence = 0.95)
    if bride != None or huntsman != None: 
        print("bride selected once!")
        if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/tradeaccepted.png', confidence = 0.85) != None:
            if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/tradebutton.png', confidence = 0.95) != None:
                tradeLoc = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/tradebutton.png', confidence = 0.85)
                print("the trade accepted, bride slected, and the trade button has been found")                
                tradeLoc = pyautogui.center(tradeLoc)
                tradeX, tradeY = tradeLoc
                print("trade loc: ", tradeLoc)
                print("trade is ready!")
                pyautogui.click(tradeX, tradeY)
                time.sleep(2)
                if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/trading?.png', confidence = 0.85) == None:
                    return True
        else:
            print("bride was found but trade accepted / button ready not found")
                

def skinTrade():
    
        while acceptTradeRequest() != True:
            acceptTradeRequest()
            print("still trying to accept request")

        time.sleep(1)

        for i in range(0,2):
            while select_My_Pixie() != True:
                select_My_Pixie()
                print("+1 pixie selected")

        time.sleep(2)

        while confirm_that_the_Item_Selected_and_Press_Trade() != True:
            confirm_that_the_Item_Selected_and_Press_Trade()
            print("still trying to confirm")
            
skinTrade()