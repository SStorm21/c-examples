import pyautogui
import time
from PIL import Image
class Unaremd:
            class  low_attack():
                def __init__ (self,basic=True,right_doge=True,leg_hit=True):
                    basic=start('d','h',interval=0.025)
                    walk=start('d',interval=0.025)
                    right_doge=start('d',"shift",interval=0.025)
                    leg_hit=start("s","h",interval=0.025)

            class chase_upper_attacks():
                def __init__ (self,up_doge=True):
                    up_doge=start('w',"shift",'h',interval=0.025)
            class simple_combo():
                def __init__ (self,jump_hit=True,instant_doge=True):
                    jump_hit=start('space',"h",interval=0.025)
                    instant_doge=start("shift"+"d",interval=0.750)
class armed:
            class sythe():
                   def __init__(sef,startt=True,attack=True,sythee1=True):
                    startt=start('d',interval=0.1)
                    attack=start("s","h",interval=0.025)
                    time.sleep(0.5)
                    sythee1=start("space")

global start
start=pyautogui.hotkey
fastest= time.sleep(0.00001953125)

time.sleep(3)
print("started!")

##Unaremd.low_attack()
##Unaremd.simple_combo()


left_side = Image.open('Untitled1.png')
side = pyautogui.screenshot()
print(side)
if side == left_side:
    print("hello world!")
else:
    print("uknown!")
print("done!")