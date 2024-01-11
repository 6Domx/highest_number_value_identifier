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

Tk.frame= Frame(root)

# 3. Functionalities

def submit():
    value_one = first_value_entry.get()
    value_two = second_value_entry.get()
    value_three = third_value_entry.get()
    
    if value_one >= value_two and value_one >= value_three:
        highest = value_one
    elif value_two >= value_one and value_two >= value_three:
        highest = value_two
    else:
        highest = value_three

    print("The highest number is", highest)

# 4. Entries and Label


# (labels)
title_label = Label(root, text=("Highest Value Identifier"), bg="#000000" , fg="#E5E9EC", font=("Airstrike", 30),bd=2)
first_value_label=Label(root,text="First Value", bg="#000000", fg="#E5E9EC",font=("Venite Adoremus Straight", 15))
second_value_label=Label(root,text="Second Value", bg="#000000", fg="#E5E9EC", font=("Venite Adoremus Straight", 15))
third_value_label=Label(root,text="Third Value", bg="#000000", fg="#E5E9EC", font=("Venite Adoremus Straight", 15))

# (label pos)
title_label.grid(row=0,column=0,columnspan=3,padx=20,pady=20)
first_value_label.grid(row=2,column=0,padx=10,pady=10)
second_value_label.grid(row=3,column=0,padx=10,pady=10)
third_value_label.grid(row=4,column=0,padx=10,pady=10)

# (entries)

first_value_entry=Entry(root, width=25, bd=5, font=("Arial Bold 15",15))
second_value_entry=Entry(root, width=25, bd=5, font=("Arial Bold 15",15))
third_value_entry=Entry(root, width=25, bd=5, font=("Arial Bold 15",15))


# (entry pos)

first_value_entry.grid(row=2,column=1,columnspan=3,padx=5,pady=5)
second_value_entry.grid(row=3,column=1,columnspan=3,padx=5,pady=5)
third_value_entry.grid(row=4,column=1,columnspan=3,padx=5,pady=5)

# (submit button)
submit_button = Button(text="SUBMIT", bg="#000000", fg="#FFFFFF", font="Franklin 12 bold", command = submit)
submit_button.grid(row=5,column=1, )


root.mainloop()