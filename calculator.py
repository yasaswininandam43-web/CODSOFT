from tkinter import *

def press(num):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current + str(num))

def Allclear():
    entry.delete(0, END)

def equal():
    result = eval(entry.get())
    entry.delete(0, END)
    entry.insert(0, result)

def delete():
    current = entry.get()
    entry.delete(len(current)-1, END)

root = Tk()
root.title("Calculator")
root.geometry("300x400")
entry = Entry(root, width=20, font=("Arial",20))
entry.grid(row=0, column=0, columnspan=4)

Button(root,text="7",command=lambda:press(7),width=5,height=2,bg='lightgrey',font='16').grid(row=1,column=0)
Button(root,text="8",command=lambda:press(8),width=5,height=2,bg='lightgrey',font='16').grid(row=1,column=1)
Button(root,text="9",command=lambda:press(9),width=5,height=2,bg='lightgrey',font='16').grid(row=1,column=2)
Button(root,text="/",command=lambda:press("/"),width=5,height=2,bg='lightgrey',font='16').grid(row=1,column=3)

Button(root,text="4",command=lambda:press(4),width=5,height=2,bg='lightgrey',font='16').grid(row=2,column=0)
Button(root,text="5",command=lambda:press(5),width=5,height=2,bg='lightgrey',font='16').grid(row=2,column=1)
Button(root,text="6",command=lambda:press(6),width=5,height=2,bg='lightgrey',font='16').grid(row=2,column=2)
Button(root,text="*",command=lambda:press("*"),width=5,height=2,bg='lightgrey',font='16').grid(row=2,column=3)

Button(root,text="1",command=lambda:press(1),width=5,height=2,bg='lightgrey',font='16').grid(row=3,column=0)
Button(root,text="2",command=lambda:press(2),width=5,height=2,bg='lightgrey',font='16').grid(row=3,column=1)
Button(root,text="3",command=lambda:press(3),width=5,height=2,bg='lightgrey',font='16').grid(row=3,column=2)
Button(root,text="-",command=lambda:press("-"),width=5,height=2,bg='lightgrey',font='16').grid(row=3,column=3)

Button(root,text="0",command=lambda:press(0),width=5,height=2,bg='lightgrey',font='16').grid(row=4,column=0)
Button(root,text="DEL",command=delete,width=5,height=2,bg='lightgrey',fg='red',font='16').grid(row=4,column=1)
Button(root,text="AC",command=Allclear,width=5,height=2,bg='lightgrey',fg='red',font='16').grid(row=4,column=2)
Button(root,text="+",command=lambda:press("+"),width=5,height=2,bg='lightgrey',font='16').grid(row=4,column=3)
Button(root,text="=",width=15,height=2,font=18,fg='red',bg='silver',command=equal).grid(row=5,column=0,columnspan=4)

root.mainloop()
