import pyautogui
import time
#pyautogui.click(518,416)
print(pyautogui.position())
##Point(x=818, y=670)
##Point(x=876, y=438) ##868,418
#if pyautogui.pixel(350, 700) ==
#print(pix)
#print(pyautogui.pixel(868, 418))
#592,332 move 48 x and -126y
#644,206
#RGB(red=0, green=92, blue=97)

#953,512 1
#998,512 2
#1086 556 8

#33 units x
#44 units y
while pyautogui.pixelMatchesColor(818, 670, (178, 177, 187)) == False:
    pyautogui.press("s")
while pyautogui.pixelMatchesColor(868, 418, (18 0, 181, 189)) == False:
    pyautogui.press("d")
    pyautogui.typewrite(['shift'])
    if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/Vault.png') != None:
        break


#954, 639

#while pyautogui.pixelMatchesColor(893, 678, (192, 192, 207)) == False:
   # pyautogui.press("s")
#while pyautogui.pixelMatchesColor(854, 427, (178, 179, 198)) == False:
   # pyautogui.press("d")
#pyautogui.typewrite(['shift'])

#go s until point below equals 
#Point(x=893, y=668)