import pyautogui
import time
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

time.sleep(2)



while True:
    pyautogui.typewrite(['enter'])
    pyautogui.hotkey('command', 'v')
    pyautogui.typewrite(['enter'])
    time.sleep(1)  
    a = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/l1.png') 
    b = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/l2.png') 
    c = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/l3.png') 
    d = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/l4.png') 
    e = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/l5.png') 
    f = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/l6.png') 
    g = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/l7.png') 
    h = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/l8.png')
    i = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/l9.png')
    #test = pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/tester.png') 
    if a != None: 
        pyautogui.click(pyautogui.center(a),button='right')
        time.sleep(0.25)
        pyautogui.move(48, -126)  
        pyautogui.click()
    if b != None: 
        pyautogui.click(pyautogui.center(b),button='right')
        time.sleep(0.25)
        pyautogui.move(48, -126)  
        pyautogui.click()
    if c != None: 
        pyautogui.click(pyautogui.center(c),button='right')
        time.sleep(0.25)
        pyautogui.move(48, -126)  
        pyautogui.click()
    if d != None: 
        print("oh")
        pyautogui.click(pyautogui.center(d),button='right')
        time.sleep(0.25)
        pyautogui.move(48, -126)  
        pyautogui.click()
    if e != None: 
        pyautogui.click(pyautogui.center(e),button='right')
        time.sleep(0.25)
        pyautogui.move(48, -126)  
        pyautogui.click()
    if f != None: 
        pyautogui.click(pyautogui.center(f),button='right')   
        time.sleep(0.25)
        pyautogui.move(48, -126)  
        pyautogui.click()
    if g != None: 
        pyautogui.click(pyautogui.center(g),button='right') 
        time.sleep(0.25)
        pyautogui.move(48, -126)  
        pyautogui.click()
    if h != None: 
        pyautogui.click(pyautogui.center(h),button='right') 
        time.sleep(0.25)
        pyautogui.move(48, -126)  
        pyautogui.click()   
    if i != None: 
        pyautogui.click(pyautogui.center(i),button='right') 
        time.sleep(0.25)
        pyautogui.move(48, -126)  
        pyautogui.click()

    if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/S_B.png') != None:
                switch_back()
                time.sleep(10)
    if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/V_I.png') != None:
                vault_inv()
                time.sleep(10)
    if pyautogui.locateOnScreen('/Users/edmond/Desktop/ROTMGBot#1/I_V.png') != None:
                inv_vault()
                time.sleep(10)