# Creating a GUI for our directory and storing the CSV files through a window.
import shutil
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from tkinter import Label
from tkinter import filedialog
from tkinter.filedialog import askopenfile

import csv, os


# Window for copying function

def window_for_copying():
    window2 = tk.Toplevel()
    window2.resizable(False, False)

    #First line to pick the file to copy
    link_label = Label(window2, text="Select CSV File To Copy : ",
                       bg="grey")
    # Box look
    link_label.grid(row=1, column=0,
                    pady=5, padx=5)


    # Showing the file selected
    window2.sourceText = Entry(window2, width=50,
                               textvariable=sourceLocation)
    # Box look
    window2.sourceText.grid(row=1, column=1,
                            pady=5, padx=5,
                            columnspan=2)


    # Choosing the file to open #1
    source_browseButton = Button(window2, text="Choose File 1",
                                 command=SourceBrowse, width=15)
    # Box look
    source_browseButton.grid(row=1, column=3,
                             pady=5, padx=5)

    # Second window for the destination directory
    destinationLabel = Label(window2, text="Destination : ",
                             bg="grey")
    # Box look
    destinationLabel.grid(row=2, column=0,
                          pady=5, padx=5)

    # Entry for chosen file and its shown output #2
    window2.destinationText = Entry(window2, width=50,
                                    textvariable=destinationLocation)
    # Box look
    window2.destinationText.grid(row=2, column=1,
                                 pady=5, padx=5,
                                 columnspan=2)

    # Choosing the file to open #2
    dest_browseButton = Button(window2, text="Choose File 2",
                               command=DestinationBrowse, width=15)
    # Box look
    dest_browseButton.grid(row=2, column=3,
                           pady=5, padx=5)


    # Action for copying and moving the file. Two buttons displayed
    copyButton = Button(window2, text="Copy File",
                        command=CopyFile, width=15)
    copyButton.grid(row=3, column=1,
                    pady=5, padx=5)

    moveButton = Button(window2, text="Move File",
                        command=MoveFile, width=15)
    moveButton.grid(row=3, column=2,
                    pady=5, padx=5)


    # Used for opening the file dialog for the user to select to copy or move using the filedialog.askopenfilenames() method.
    # Since you can select multiple files, we converted the selections to lists.
def SourceBrowse():

    window2.files_list = list(
        filedialog.askopenfilenames(initialdir="C:/Users/oliviarazzo/Downloads/Group11/Python_code"))

    # Displaying the selected files in the window2.sourceText
    # Entry using window2.sourceText.insert()
    window2.sourceText.insert('1', window2.files_list)


    # Used for opening the file dialog for the user to select to destination file using the filedialog.askdirectory() method.
    # Since you can select multiple files, we converted the selections to lists.
def DestinationBrowse():

    destinationdirectory = filedialog.askdirectory(
        initialdir="C:/Users/oliviarazzo/Downloads/Group11/Python_code")

    # Displaying the selected directory in the window2.destinationText Entry using
    # window2.destinationText.insert()
    window2.destinationText.insert('1', destinationdirectory)


    # Retrieve the source file selected by SourceBrowse() function and storing it in files_list for the loop described below.
def CopyFile():
    files_list = window2.files_list


    # Variable destination location is used to retrieve the destination location from the textvariable using get() method
    # and storing it in destination location variable
    destination_location = destinationLocation.get()

    # Looping through the files present in the list
    for f in files_list:

        # Used for copying the file to the destination chosen as described in the get() method above. We use copy() method
        # from the shutil module which takes the source file and destination as arguments.
        shutil.copy(f, destination_location)


    messagebox.showinfo("SUCCESSFUL")


    # Retrieve the source file selected by SourceBrowse() function and storing it in files_list for the loop described below.
def MoveFile():
    files_list = window2.files_list

    # Variable destination location is used to retrieve the destination location from the textvariable using get() method
    # and storing it in destination location variable same as the copy function.
    destination_location = destinationLocation.get()

    # Looping through the files present in the list
    for f in files_list:
        # Moving the file to the destination using
        # the move() of shutil module copy take the
        # source file and the destination folder as
        # the arguments
        shutil.move(f, destination_location)

    messagebox.showinfo("SUCCESSFUL")


# THIS IS THE FIRST WINDOW DISPLAYED FOR SHOWING ALL AVAILABLE FILES IN THE DIRECTORY GIVEN!!
# Choice for copying or opening a file through file dialog
window = tk.Tk()

# Basic setup of window
window.title("Pick & Place File Vault")
window.geometry("400x700")
window.resizable(False, False)

# Text in the window
label1 = Label(window,
               text="Choose a file to open",
               font=("Arial", 15)
               )
label1.pack(padx=10, pady=20)

# Showing files in the folder
file_view = tk.Listbox(window)
file_view.pack(expand=tk.YES, fill=tk.BOTH)

file_location = "/Users/oliviarazzo/Downloads/Group11/Python_code"
for items in os.listdir(file_location):
    file_view.insert(0, items)

# Button for opening a file and showing the dialog directory
def openfile():
    return filedialog.askopenfilename()
button = ttk.Button(window, text="Open", command=openfile)  # <------
button.pack()

# Button for the copying window to open up
button2 = ttk.Button(window, text="Copy",
                     command=lambda: window_for_copying())
button2.pack()


# Keeps the window open and does not close it
# Main function
window2 = tk.Tk()

# Creating tkinter variable
sourceLocation = StringVar()
destinationLocation = StringVar()

# Defining infinite loop
window2.mainloop()
