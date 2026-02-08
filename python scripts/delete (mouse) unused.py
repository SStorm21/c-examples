import pyautogui
import time
from customtkinter import *

root = CTk()
root.geometry("400x400")
def delete():#main massage
    #timing
    time.sleep (2)
    ##message
    #write it
    #pyautogui.moveTo(1018,983)
    #pyautogui.leftClick(1018,983)
    ##delete it
    #More
    pyautogui.moveTo(1534,331)
    pyautogui.leftClick(1534,333)
    pyautogui.moveTo(1625,903)
    pyautogui.leftClick(1625,903)
    #click it
    pyautogui.moveTo(1557,955)
    pyautogui.leftClick(1557,955)
    #delete it!
    pyautogui.moveTo(1114,647)
    pyautogui.leftClick(1114,647)
def delete2():
        #timing
    time.sleep (2)
    ##message
    #write it
    #pyautogui.moveTo(1018,983)
    #pyautogui.leftClick(1018,983)
    ##delete it
    #More
    pyautogui.moveTo(1534,331)
    pyautogui.leftClick(1534,333)
    pyautogui.moveTo(491,945)
    pyautogui.leftClick(491,945)
    #click it
    #pyautogui.moveTo(1557,955)
    #pyautogui.leftClick(1557,955)
    #delete it!
    #pyautogui.moveTo(1114,647)
    #pyautogui.leftClick(1114,647)

btn = CTkButton(root,text="DELETE",command=delete)
btn.pack(side=TOP)
btn = CTkButton(root,text="DELETE!!",command=delete2)
btn.pack(side=TOP)
root.mainloop()
#write 1
#send

