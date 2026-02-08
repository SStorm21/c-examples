from customtkinter import *
import pyautogui
import time
root = CTk()
root.config(bg="black")
root.geometry("800x600")
#Defnations
def DeleteLast():
    time.sleep(1)
    # مسح رسايل عربية
    pyautogui.hotkey('up')
    pyautogui.hotkey('ctrl','a')
    pyautogui.hotkey('delete','enter')
    pyautogui.hotkey('down','enter')
corner = 11
QuickVanish = CTkTabview(root,text_color="blue"
                         ,segmented_button_fg_color='blue',
                         segmented_button_unselected_hover_color="black",
                         segmented_button_selected_hover_color="white",
                         segmented_button_selected_color="white",
                         segmented_button_unselected_color="black",
                         border_width=3,
                         corner_radius=corner,
                         border_color="blue",
                         fg_color="black"       
)

QuickVanish.add('QuickVanish')
QuickVanish.add('tab                                                        2')
QuickVanish.add('tab3')
QuickVanish.add('tab4')
QuickVanish.add('tab5')
QuickVanish.add('tab6')
QuickVanish.add('tab8')
QuickVanish.add('tab9')
QuickVanish.add('tab10')
QuickVanish.add('tab11')
QuickVanish.add('tab12')
QuickVanish.pack(fill=BOTH,expand=1)

Qframe = CTkFrame(QuickVanish.tab('QuickVanish'),
                  width=667,height=520,
                  border_width=3,corner_radius=corner
                  ,border_color="blue",fg_color="black"
                  )
Qframe.pack()
#delete last message
delett = CTkFrame(Qframe,
                  width=338,height=74,
                  border_width=3,corner_radius=corner
                  ,border_color="blue",fg_color="black"
                  )
delett.place(x=300,y=430)
dlmButton = CTkButton(delett,text="Delete",
                      font=((),15,"bold"),
                      corner_radius=100,
                      bg_color="black",
                      text_color="blue",
                      hover_color="white",
                      border_width=5,
                      border_color="blue",
                      fg_color="black",
                      command=DeleteLast
                      )
dlmButton.place(x=175,y=20)
#timer
timer = CTkFrame(Qframe,
                  width=121,height=52,
                  border_width=3,corner_radius=corner
                  ,border_color="blue",fg_color="black"
                  )
timer.place(x=20,y=450)
#Message 
message =  CTkFrame(Qframe,
                  width=626,height=307,
                  border_width=3,corner_radius=corner
                  ,border_color="blue",fg_color="black"
                  )
message.place(x=20,y=110)

root.mainloop()