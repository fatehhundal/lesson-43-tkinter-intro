from tkinter import *

window = Tk()
window.title("Random Password Generator")
window.geometry("960x540")

title = Label(text="Random Password Generator", font=("Arial", 35), fg="black")
description = Label(text="Are you tired of coming up with your own passwords? Then you've come to the right website. This page generates random passwords for you to use for any accounts you make.", font=("Arial", 10), fg="black")
command = Label(text="Click the button below to generate a strong, secure password.", font=("Arial", 20), fg="black")
button = Button(text="Click me", fg="black", bg="white")
entry = Entry(fg="black", bg="white", width=55)
title.pack()
description.pack()
command.pack()
button.pack()
entry.pack()

window.mainloop()