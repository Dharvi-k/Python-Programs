# Importing required libraries
import tkinter as tk    # tkinter is used to create the GUI window.
from time import strftime

root=tk.Tk()
root.title("Digital Clock")

# Defining time updating functions
def time():
    string=strftime('%H:%M:%S %p \n %D')
    label.config(text=string)
    label.after(1000,time)

#   Create Label to Show Time
label=tk.Label(root,font=('calibri',30,'bold'),background='white',foreground='black')
label.pack(anchor='center')

# Start the clock
time()

# Keep the window open
root.mainloop()