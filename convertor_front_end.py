from tkinter import *

def change():
    

window=Tk()

window.wm_title("convertor")

l1=Label(window,text="Path")
l1.grid(row=0,column=0)

title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

l2=Label(window,text="spaces")
l2.grid(row=0,column=2)

Space_text=StringVar()
e2=Entry(window,textvariable=Space_text)
e2.grid(row=0,column=3)

b1=Button(window,text="view all",width=12,command=change)
b1.grid(row=2,column=3)

window.mainloop()
