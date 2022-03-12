from cProfile import label
from cgitb import text
import tkinter as tk  # main obrary for UI
from tkinter import Button, Canvas, PhotoImage, filedialog,Text 
import os
from tkinter import font
from turtle import width

root  = tk.Tk()   # to get a window
root.geometry("400x400")
root.minsize(800,700)
root.maxsize(800,700)

photo = PhotoImage(file="BGimage.png")

# placing the image in background
bg_label = tk.Label(image=photo)
bg_label.place(x=0,y=0,relwidth=1,relheight=1)

# add some text over the backgound image
my_data = tk.Label(root, text="Welcome!", font=("Helvetica", 50), fg="black",bg="#fef8ea")
my_data.pack(pady=50)

my_text=Text(root,width=30,height=1,font=("Helvetica",25))
my_text.pack(pady=20)
# adding buttons over the image
next_frame = tk.Frame(root)
next_frame.pack()

button1 = Button(next_frame, text="Go",bg="#fef8ea")
button1.grid(row=0, column=0, padx=5)


root.mainloop()