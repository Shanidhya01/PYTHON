from tkinter import *  # type: ignore # standard GUI (Graphical User Interface) toolkit.
import pyperclip        # allows us to copy text to the clipboard.
import random
root = Tk()                # initializing the tkinter
root.geometry("600x400")   # setting the width and height of the gui
passstr = StringVar()      # variable will be used to store the password generated
passlen = IntVar()         # store the length of the password entered by the user
passlen.set(0)
def generate():         # function to generate the password
    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
            'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', 
            '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&', 
            '*', '(', ')']
    password = ""
    for x in range(passlen.get()):   # loop to generate the random password of the length entered by the user
        password = password + random.choice(pass1)
    passstr.set(password)            # setting the password to the entry widget
def copytoclipboard():
    random_password = passstr.get()
    pyperclip.copy(random_password)
# Creating a text label widget
Label(root, text="Password Generator Application", font="calibri 25 bold").pack()
Label(root, text="Enter password length").pack(pady=3)
Entry(root, textvariable=passlen).pack(pady=3)
Button(root, text="Generate Password", command=generate).pack(pady=7)
Entry(root, textvariable=passstr).pack(pady=3)
Button(root, text="Copy to clipboard", command=copytoclipboard).pack()
root.mainloop()