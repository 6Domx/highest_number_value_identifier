# TASK:
# Ask user to input 3 numbers, find and print the biggest number using only if statements.

# Pseudocode
# Ask users to input at least 3 numbers.
# Evaluate the numbers using mainly "if" statements.
# Print the number that is highest in its value.

# MAIN CODE
# 1. Imports

import sqlite3
from tkinter import *
from tkinter import Tk
from tkinter import messagebox
from PIL import ImageTk, Image

# 2. Window Configuration

root = Tk()
root.title("Highest Number Value Identifier")
root.geometry("600x480")
image_0=Image.open("C:\\Users\\M2\\Documents\\CODES\\Projects\\PYTHON\\highest_number_value_identifier\\image.png")
bck_end=ImageTk.PhotoImage(image_0)
lbl=Label(root,image=bck_end)
lbl.place(x=0,y=0)
root.resizable(False,False)

root.mainloop()