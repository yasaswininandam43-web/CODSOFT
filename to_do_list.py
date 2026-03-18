from tkinter import *

def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(END, task)
        entry.delete(0, END)

def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)

root = Tk()
root.title("To-Do List")
root.geometry("300x350")

entry = Entry(root, width=25, font=("Arial",14))
entry.pack(pady=10)

add_btn = Button(root, text="Add Task", width=15, command=add_task)
add_btn.pack(pady=5)

listbox = Listbox(root, width=30, height=10)
listbox.pack(pady=10)

del_btn = Button(root, text="Delete Task", width=15, command=delete_task)
del_btn.pack(pady=5)

root.mainloop()
