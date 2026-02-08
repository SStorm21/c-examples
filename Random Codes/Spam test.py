import pyautogui
import time
import string
import random
time.sleep(2)
x=1
while 1:
    if x<10:
        x+=1
        print('@sent!')
        #message = ''.join(random.choices(string.ascii_letters,k=700))
        pyautogui.hotkey('ctrl','v')
        pyautogui.hotkey('enter')
        if x ==10:
            print("Done!")
            break
