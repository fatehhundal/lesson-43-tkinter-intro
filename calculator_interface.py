from tkinter import *

root = Tk()
root.title("Calculator")

entry = Entry(root, font=("Arial", 20), bd=10, relief=RIDGE, justify=RIGHT)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

Button(root, text="7", font=("Arial", 18), width=4, height=2).grid(row=1, column=0, padx=5, pady=5)
Button(root, text="8", font=("Arial", 18), width=4, height=2).grid(row=1, column=1, padx=5, pady=5)
Button(root, text="9", font=("Arial", 18), width=4, height=2).grid(row=1, column=2, padx=5, pady=5)
Button(root, text="/", fg="white", bg="black", font=("Arial", 18), width=4, height=3).grid(row=1, column=3, padx=5, pady=5)

Button(root, text="4", font=("Arial", 18), width=4, height=2).grid(row=2, column=0, padx=5, pady=5)
Button(root, text="5", font=("Arial", 18), width=4, height=2).grid(row=2, column=1, padx=5, pady=5)
Button(root, text="6", font=("Arial", 18), width=4, height=2).grid(row=2, column=2, padx=5, pady=5)
Button(root, text="*", fg="white", bg="black", font=("Arial", 18), width=4, height=2).grid(row=2, column=3, padx=5, pady=5)

Button(root, text="1", font=("Arial", 18), width=4, height=2).grid(row=3, column=0, padx=5, pady=5)
Button(root, text="2", font=("Arial", 18), width=4, height=2).grid(row=3, column=1, padx=5, pady=5)
Button(root, text="3", font=("Arial", 18), width=4, height=2).grid(row=3, column=2, padx=5, pady=5)
Button(root, text="-", fg="white", bg="black", font=("Arial", 18), width=4, height=2).grid(row=3, column=3, padx=5, pady=5)

Button(root, text="0", font=("Arial", 18), width=4, height=2).grid(row=4, column=0, padx=5, pady=5)
Button(root, text=".", font=("Arial", 18), width=4, height=2).grid(row=4, column=1, padx=5, pady=5)
Button(root, text="=", fg="white", bg="black", font=("Arial", 18), width=4, height=2).grid(row=4, column=2, padx=5, pady=5)
Button(root, text="+", fg="white", bg="black", font=("Arial", 18), width=4, height=2).grid(row=4, column=3, padx=5, pady=5)

Button(root, text="C", fg="white", bg="red", activebackground="red", font=("Arial", 18), width=18, height=2).grid(row=5, column=0, columnspan=4, pady=5)

root.mainloop()