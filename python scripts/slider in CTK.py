from tkinter import *

master = Tk()
w2 = Scale(master, from_=0, to=100, orient=HORIZONTAL)
w2.set(1)
w2.pack()

mainloop()