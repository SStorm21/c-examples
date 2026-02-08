import string
import random
import os
import time 
import pyautogui
N = 5
 
res = ''.join(random.choices(string.ascii_uppercase+string.ascii_lowercase+
                             string.digits, k=N))
 
res2 = ''.join(random.choices(string.ascii_uppercase+string.ascii_lowercase+
                             string.digits, k=N))

link = "www.instagram.com/_n/web_emaillogin?uid="+str(res2)+"&token=" + str(res)+"&auto_send=0"

os.system("start cmd")
time.sleep(2)
pyautogui.write('start '+link,interval=0.025)
pyautogui.press("enter")
#pyautogui.hotkey(link)
