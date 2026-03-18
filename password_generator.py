from tkinter import *
import random
import string

def generate_password():
    length = int(length_input.get())
    chars = string.ascii_letters + string.digits
    password = ""
    for i in range(length):
        ch = random.choice(chars)
        password = password + ch
    password_display.config(text=password)

root = Tk()
root.title("My Password Generator")
root.geometry("300x350")
Label(root, text="Enter password length").pack()
length_input = Entry(root)
length_input.pack()

Button(root, text="Generate Password", command=generate_password,bg='yellow').pack()

password_display = Label(root, text="")
password_display.pack()

root.mainloop()
