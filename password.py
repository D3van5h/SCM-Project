from tkinter import *
import pyperclip
import random

root = Tk()

root.attributes("-fullscreen",True)
root.title(" Random Password Generator")

passwrd = StringVar()
passlen = IntVar()

passlen.set(0)
def generate():

    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D','E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
             'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X','Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
             '9', '0','!', '@', '#', '$', '%', '^', '&','*', '(', ')']
    password = ""
    for x in range(passlen.get()):
        password = password + random.choice(pass1)
    passwrd.set(password)

def copyclipboard():
    random_password = passwrd.get()
    pyperclip.copy(random_password)


Label(root, text="Password Generator", font="Courier 50 bold").pack()
Label(root, text="").pack()
Label(root, text="").pack()
Label(root, text="").pack()
Label(root, text="").pack()
Label(root, text="").pack()
Label(root, text="Enter the length of your password",font="Courier 35 italic").pack(pady=3)
Entry(root, textvariable=passlen).pack(pady=3)
Button(root, text="Get password",font="Courier 15 italic",command=generate,bg="light grey",borderwidth=5).pack(pady=7)
Entry(root, textvariable=passwrd).pack(pady=3)
Button(root, text="Copy to clipboard",font="Courier 15 italic", command=copyclipboard,bg="light grey",borderwidth=5).pack()

root.mainloop()
