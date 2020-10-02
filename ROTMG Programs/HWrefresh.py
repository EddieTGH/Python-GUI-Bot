import pyautogui
import time
import cv2
from twilio.rest import Client
#bot to use when I am on adj window to refresh trades
#must have 6 tabs open
pyautogui.click(223,45)

x = 0
while True:
        #pyautogui.hotkey('command', 'tab')
        time.sleep(1)
        pyautogui.click(441,40) #tab 2
        time.sleep(1)
        pyautogui.click(518,416) #publish offers button
        time.sleep(2)           
        pyautogui.click(223,40) #tab one
        time.sleep(1)
        pyautogui.click(800,400) #middle of screen 
        pyautogui.typewrite(['tab'])
        time.sleep(1)
        pyautogui.typewrite(['tab'])
        time.sleep(1)
        pyautogui.typewrite(['tab'])
        time.sleep(2)
        pyautogui.click(800,400)
        #pyautogui.typewrite(['r'])
        #pyautogui.hotkey('command', 'tab')
        time.sleep(120)

