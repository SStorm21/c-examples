import customtkinter
from customtkinter import *
root = CTk()

root.geometry("333x300+900+200")
root.title("test")

def ref():#refresh
    pass
def button2():
    button_2= CTkButton(root,text="am button 2").place(x=50,y=50)
def button3():
    button_3= CTkButton(root,text="am button 3").place(x=50,y=50)

button = CTkButton(root,text="refresh",command=ref).place(x=10,y=10) #import

button_= CTkButton(root,text="spawn button 2 ",command=button2).place(x=10,y=50)
button_3= CTkButton(root,text="spawn button 3",command=button3).place(x=10,y=100)

root.mainloop()