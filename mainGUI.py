# Creating a GUI for our directory and storing the CSV files through a window.
import shutil
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from tkinter import Label
from tkinter import filedialog
from tkinter.filedialog import askopenfile

import csv, os

# Store directory folder in file_location variable
file_location = os.getcwd()

# Name of the folder where output is stored
new_folder = "\Output"
new_files = file_location + new_folder

# Check whether the specified path exists or not
isExist = os.path.exists(new_files)

if not isExist:
  # Create a new directory because it does not exist 
  os.makedirs(new_files)
  print("The new directory is created!")

window = tk.Tk()

# Basic setup of window
window.title("Pick & Place File Vault")
window.geometry("400x700")
window.resizable(False, False)

# Text in the window
label1 = Label(window,
               text="Choose a File",
               font=("Arial", 15)
               )
label1.pack(padx=10, pady=20)

# Showing files in the folder
file_view = tk.Listbox(window)
file_view.pack(expand=tk.YES, fill=tk.BOTH)

for items in os.listdir(file_location):
    if items.endswith(".csv"):      # Only shows csv files
        file_view.insert(0, items)

# Placeholder function that copies selected csv file into the output folder. Will be replaced by our sorting code later
def do_something(sourcefile):
    pre, ext = os.path.splitext(sourcefile)
    original = file_location + "\\" + sourcefile
    target = new_files +"\\" + pre + "_new" + ext
    shutil.copyfile(original, target)

# Function for storing the selected listbox value and then runs do_something
def selected_item():
    # Traverse the tuple returned by curselection method and store corresponding value in the listbox
    for i in file_view.curselection():
        sourcefile = file_view.get(i)
    do_something(sourcefile)

button = tk.Button(window, text='Copy Selected',command=lambda: selected_item())
button.pack()

# Defining infinite loop
window.mainloop()
