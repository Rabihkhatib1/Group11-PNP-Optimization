import csv
from math import sqrt
import os
import random
from re import S

import shutil
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from tkinter import Label
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from turtle import left, width
import sys
import keyboard

from numpy import column_stack

import tkinter as tk

class CreateToolTip(object):
    """
    create a tooltip for a given widget
    """
    def __init__(self, widget, text='widget info'):
        self.waittime = 500     #miliseconds
        self.wraplength = 180   #pixels
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<ButtonPress>", self.leave)
        self.id = None
        self.tw = None

    def enter(self, event=None):
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.showtip)

    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)

    def showtip(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        # creates a toplevel window
        self.tw = tk.Toplevel(self.widget)
        # Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(self.tw, text=self.text, justify='left',
                       background="#ffffff", relief='solid', borderwidth=1,
                       wraplength = self.wraplength)
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tw
        self.tw= None
        if tw:
            tw.destroy()

""" tk_ToolTip_class101.py
gives a Tkinter widget a tooltip as the mouse is above the widget
tested with Python27 and Python34  by  vegaseat  09sep2014
www.daniweb.com/programming/software-development/code/484591/a-tooltip-class-for-tkinter

Modified to include a delay time by Victor Zaccardo, 25mar16
"""

class Redirect():
    
    def __init__(self, widget):
        self.widget = widget
    
    def write(self, text):
        self.widget.insert('end', text)
        self.widget.see('end') # autoscroll
   

def print_t(string):
    old_stdout = sys.stdout    
    sys.stdout = Redirect(text)
    print(string)
    sys.stdout = old_stdout

##############################################################################################################################################
# MAIN
##############################################################################################################################################

RUNS = 10000
file_location = os.getcwd()
Footprint_Library = file_location + "/Data/Footprint_Library.csv"
Compdata = file_location + "/Data/Compdata.csv"
Feeder = file_location + "/Data/Feeder.csv"
Mark = file_location + "/Data/Mark.csv"
Nozzle = file_location + "/Data/Nozzle.csv"
Panel = file_location + "/Data/Panel.csv"
PCBdata = file_location + "/Data/PCB.csv"

import_table = []
Footprint_Library_table = list(csv.reader(open(Footprint_Library)))
Compdata_table = list(csv.reader(open(Compdata)))
F_table = list(csv.reader(open(Feeder)))
M_table = list(csv.reader(open(Mark)))
N_table = list(csv.reader(open(Nozzle)))
P_table = list(csv.reader(open(Panel)))
PCB_table = list(csv.reader(open(PCBdata)))

#######################################################################
# Recommends Nozzles to use. Does not change the current nozzles 
# unless a specific nozzle type is missing. 
#######################################################################
def Nozzle_Suggest(import_table,Footprint_Library_table,N_table):
    nozzle_array = ["CN030","CN040","CN065","CN100","CN140","CN220","CN400","CN750"]

    nozzle_CN030 = 0
    nozzle_CN040 = 0
    nozzle_CN065 = 0
    nozzle_CN100 = 0
    nozzle_CN140 = 0
    nozzle_CN220 = 0
    nozzle_CN400 = 0
    nozzle_CN750 = 0

    F_col = []

    for i in range(len(Footprint_Library_table)):
        F_col.append(Footprint_Library_table[i][0])

    for i in range(1,len(import_table)):
        if(import_table[i][1] not in F_col):
            print_t(import_table[i][1] + " is not in Footprint_Library.csv")
            return False
        index = F_col.index(import_table[i][1])
        if Footprint_Library_table[index][4] == "CN030":
            nozzle_CN030 += 1
        elif Footprint_Library_table[index][4] == "CN040":
            nozzle_CN040 += 1
        elif Footprint_Library_table[index][4] == "CN065":
            nozzle_CN065 += 1
        elif Footprint_Library_table[index][4] == "CN100":
            nozzle_CN100 += 1
        elif Footprint_Library_table[index][4] == "CN140":
            nozzle_CN140 += 1
        elif Footprint_Library_table[index][4] == "CN220":
            nozzle_CN220 += 1
        elif Footprint_Library_table[index][4] == "CN400":
            nozzle_CN400 += 1
        elif Footprint_Library_table[index][4] == "CN750":
            nozzle_CN750 += 1

    nozzle_CN030round = 0
    nozzle_CN040round = 0
    nozzle_CN065round = 0
    nozzle_CN100round = 0
    nozzle_CN140round = 0
    nozzle_CN220round = 0
    nozzle_CN400round = 0
    nozzle_CN750round = 0
    total = 0

    total_nozzles = nozzle_CN030 + nozzle_CN040 + nozzle_CN065 + nozzle_CN100 + nozzle_CN140 + nozzle_CN220 + nozzle_CN400 + nozzle_CN750

    if (nozzle_CN030 > 0):
        nozzle_CN030round = round((nozzle_CN030 / total_nozzles) * 8)
        # If round is 0
        total += nozzle_CN030round
        if nozzle_CN030round == 0:
            nozzle_CN030round += 1
            total += nozzle_CN030round

    if (nozzle_CN040 > 0):
        nozzle_CN040round = (round((nozzle_CN040 / total_nozzles) * 8))
        total += nozzle_CN040round
        # If round is 0
        if nozzle_CN040round == 0:
            nozzle_CN040round += 1
            total += nozzle_CN040round

    if (nozzle_CN065 > 0):
        nozzle_CN065round = round((nozzle_CN065 / total_nozzles) * 8)
        total += nozzle_CN065round
        # If round is 0
        if nozzle_CN065round == 0:
            nozzle_CN065round += 1
            total += nozzle_CN065round

    if (nozzle_CN100 > 0):
        nozzle_CN100round = round((nozzle_CN100 / total_nozzles) * 8)
        total += nozzle_CN100round
        #If round is 0
        if nozzle_CN100round == 0:
            nozzle_CN100round += 1
            total += nozzle_CN100round

    if (nozzle_CN140 > 0):
        nozzle_CN140round = round((nozzle_CN140 / total_nozzles) * 8)
        # If round is 0
        total += nozzle_CN140round
        if nozzle_CN140round == 0:
            nozzle_CN140round += 1
            total += nozzle_CN140round

    if (nozzle_CN220 > 0):
        nozzle_CN220round = round((nozzle_CN220 / total_nozzles) * 8)
        total += nozzle_CN220round
        # If round is 0
        if nozzle_CN220round == 0:
            nozzle_CN220round += 1
            total += nozzle_CN220round

    if (nozzle_CN400 > 0):
        nozzle_CN400round = round((nozzle_CN400 / total_nozzles) * 8)
        total += nozzle_CN400round
        # If round is 0
        if nozzle_CN400round == 0 :
            nozzle_CN400round += 1
            total += nozzle_CN400round

    if (nozzle_CN750 > 0):
        nozzle_CN750round = round((nozzle_CN750 / total_nozzles) * 8)
        total += nozzle_CN750round
        # If round is 0
        if nozzle_CN750round == 0 :
            nozzle_CN750round += 1
            total += nozzle_CN750round

    nozzle_total_array = [nozzle_CN030round,nozzle_CN040round,nozzle_CN065round,nozzle_CN100round,nozzle_CN140round,nozzle_CN220round,nozzle_CN400round,nozzle_CN750round]

    while total > 8:
        index_max = max(range(len(nozzle_total_array)), key=nozzle_total_array.__getitem__)
        nozzle_total_array[index_max] -= 1
        total -= 1
        nozzle_array[index_max]
    while total < 8:
        index_max = max(range(len(nozzle_total_array)), key=nozzle_total_array.__getitem__)

    nozzle_counter_array = []
    for i in range(len(nozzle_total_array)):
        to_append = []
        to_append.append(nozzle_array[i])
        to_append.append(nozzle_total_array[i])
        nozzle_counter_array.append(to_append)
    nozzle_counter_array.sort(key=lambda x:x[1],reverse=True)

    nozzle_suggest_array = []
    for i in range(len(nozzle_counter_array)):
        while(nozzle_counter_array[i][1] > 0):
            nozzle_suggest_array.append(nozzle_counter_array[i][0])
            nozzle_counter_array[i][1] -= 1

    print_t("Recommended Nozzles: " + nozzle_suggest_array[0] + ", " + nozzle_suggest_array[1] + ", " + nozzle_suggest_array[2] + ", " + nozzle_suggest_array[3] + ", " + nozzle_suggest_array[4] + ", " + nozzle_suggest_array[5] + ", " + nozzle_suggest_array[6] + ", " + nozzle_suggest_array[7])
    print_t("Current Nozzles: " + N_table[1][2] + ", " + N_table[2][2] + ", " + N_table[3][2] + ", " + N_table[4][2] + ", " + N_table[5][2] + ", " + N_table[6][2] + ", " + N_table[7][2] + ", " + N_table[8][2])
    window.update()
    window.after(20)
    N_table_array = [N_table[1][2],N_table[2][2],N_table[3][2],N_table[4][2],N_table[5][2],N_table[6][2],N_table[7][2],N_table[8][2]]
    for i in range(len(nozzle_suggest_array)):
        if nozzle_suggest_array[i] not in N_table_array:
            print_t("Using Recommended Nozzles.")
            window.update()
            window.after(20)
            N_table[1][2] = nozzle_suggest_array[0]
            N_table[2][2] = nozzle_suggest_array[1]
            N_table[3][2] = nozzle_suggest_array[2]
            N_table[4][2] = nozzle_suggest_array[3]
            N_table[5][2] = nozzle_suggest_array[4]
            N_table[6][2] = nozzle_suggest_array[5]
            N_table[7][2] = nozzle_suggest_array[6]
            N_table[8][2] = nozzle_suggest_array[7]
            return N_table
    print_t("Using Current Nozzles.")
    window.update()
    window.after(20)            
    return N_table

#######################################################################
# Checks if footprints and comments are persent in Compdata.csv
# discards component otherwise.
#######################################################################
def Check_footprints_comments(table_check,Compdata_table):
    Compdata_fp_cmnt = []
    table_check_fp_cmnt = []
    discard = []
    check = 0
    for i in range(len(Compdata_table)):
        to_append = []
        to_append.append(Compdata_table[i][0])
        to_append.append(Compdata_table[i][1])
        Compdata_fp_cmnt.append(to_append)
    for i in range(len(table_check)):
        to_append = []
        to_append.append(table_check[i][1])
        to_append.append(table_check[i][10])
        table_check_fp_cmnt.append(to_append) 
        if table_check_fp_cmnt[i] in Compdata_fp_cmnt:
            continue
        else:
            check += 1
            discard.append(i)
            print_t("Discarded "+ table_check[i][1])
            print_t("Add Component '" + table_check_fp_cmnt[i][0] + "' - '" + table_check_fp_cmnt[i][1] + "' to Data/Compdata.csv" )
            window.update()
        window.after(50)    
    for i in range(len(discard)):    
        table_check.remove(table_check[discard[i]])
    
    return table_check

#######################################################################
# If the Import file is pre-made and only needs the nozzle/feeder
# order to be modified, then this function replaces all the Panel, 
# Mark, PCB, Nozzle data with that the datafile.
#######################################################################
def Existing_Table(table_check,Compdata_table,M_table,N_table,P_table,PCB_table):
    col1 =[]
    import_table = []
    import_table_temp = []
    Compdata_table_temp = []
    for i in range(len(table_check)):
        col1.append(table_check[i][0])
    Compdata_index = col1.index('#Feeder')
    PCB_index = col1.index('#PCB')
    P_index = col1.index('#Panel')
    N_index = col1.index('#Nozzle')
    M_index = col1.index('#Mark')
    Foot_index = col1.index('#Comp')
    Compdata_end = PCB_index - 1
    PCB_end = P_index - 1
    P_end = N_index - 1
    N_end = M_index - 1
    M_end = Foot_index - 1
    Foot_end = len(col1)

    for i in range(Compdata_index,Compdata_end):
        Compdata_table_temp.append(table_check[i])
    for i in range(PCB_index,PCB_end):
        PCB_table.append(table_check[i])
    for i in range(P_index,P_end):
        P_table.append(table_check[i])
    for i in range(N_index,N_end):
        N_table.append(table_check[i])
    for i in range(M_index,M_end):
        M_table.append(table_check[i])
    for i in range(Foot_index,Foot_end):
        import_table_temp.append(table_check[i])

    for i in range(len(Compdata_table_temp)):
        to_append = []
        for j in range(6,len(Compdata_table_temp[i])):
            if j != 8:
                to_append.append(Compdata_table_temp[i][j])
        Compdata_table.append(to_append)

    import_table.append(["Designator","Footprint","Center-X(mm)","Center-Y(mm)","Ref-X(mm)","Ref-Y(mm)","Pad-X(mm)","Pad-Y(mm)","Layer","Rotation","Comment"])
    for i in range(1,len(import_table_temp)):
        to_append = []
        to_append.append(import_table_temp[i][4])
        to_append.append(import_table_temp[i][3])
        to_append.append(import_table_temp[i][6])
        to_append.append(import_table_temp[i][7])
        to_append.append(import_table_temp[i][6])
        to_append.append(import_table_temp[i][7])
        to_append.append(import_table_temp[i][6])
        to_append.append(import_table_temp[i][7])
        to_append.append("Toplayer")
        to_append.append(import_table_temp[i][8])
        to_append.append(import_table_temp[i][2])
        import_table.append(to_append)
    return import_table,Compdata_table,M_table,N_table,P_table,PCB_table

sourcefile = ''
# Store directory folder in file_location variable
file_location = os.getcwd()

import_folder = "/Import"
import_file_location = file_location + import_folder

# Name of the folder where output is stored
new_folder = "/Output"
new_files = file_location + new_folder

# Check whether the specified path exists or not
isExist = os.path.exists(new_files)

if not isExist:
  # Create a new directory because it does not exist 
  os.makedirs(new_files)
  print("The new directory is created!")

Footprint_Nozzle = []
to_fappend = []
for i in range(len(Footprint_Library_table)):
    to_fappend.append(Footprint_Library_table[i][0])
Footprint_Nozzle.append(to_fappend)
to_fappend = []
for i in range(len(Footprint_Library_table)):
    to_fappend.append(Footprint_Library_table[i][4])
Footprint_Nozzle.append(to_fappend)

#######################################################################
# Measures the distance between each feeder or a feeder and the center
# start is the starting feeder and end is the ending feeder
# if start is set to 0, it is considered to be the center.
#######################################################################
def distance_calc(start,end):
    dist = 0
    t = 0

    if start == end:
        dist = 0.1
        dist = dist*20.9
        dist = round(dist,2)
        return float(str(round(dist,2)))

    if start == 0:
        if (end <= 17):
            t = abs(17-end)+2.5
            dist = sqrt(144+(t*t))
            dist = round(dist,2)
        elif (end <= 33):
            t = abs(33-end)+2.5
            dist = sqrt(144+(t*t))
            dist = round(dist,2)
        elif (end <= 50):
            t = abs(50-end)+2.5
            dist = sqrt(144+(t*t))
            dist = round(dist,2)
        elif (end <= 66):
            t = abs(66-end)+2.5
            dist = sqrt(144+(t*t))
            dist = round(dist,2)
        dist = dist*20.9

        dist = round(dist,2)
        return float(str(round(dist,2)))

    if (start <= 17):
        if (end <= 17):
            dist = abs(end - start)
        elif (end <= 33):
            dist = abs((end-start))+5
        elif (end <= 50):
            t = abs(end-(start+33))
            dist = sqrt(576+(t*t))
            dist = round(dist,2)
        elif (end <= 66):
            t = abs((end-(start+33)))+5
            dist = sqrt(576+(t*t))
            dist = round(dist,2)
    elif (start <= 33):
        if (end <= 17):
            dist = abs((end - start))+5
        elif (end <= 33):
            dist = abs(end-start)
        elif (end <= 50):
            t = abs((end-(start+33)))+5
            dist = sqrt(576+(t*t))
            dist = round(dist,2)
        elif (end <= 66):
            t = abs(end-(start+33))
            dist = sqrt(576+(t*t))
            dist = round(dist,2)
    elif (start <= 50):
        if (end <= 17):
            t = abs(end-(start-33))
            dist = sqrt(576+(t*t))  
            dist = round(dist,2)        
        elif (end <= 33):
            t = abs((end-(start-33)))+5
            dist = sqrt(576+(t*t)) 
            dist = round(dist,2) 
        elif (end <= 50):
            dist = abs(end - start)
        elif (end <= 66):
            dist = abs((end-start))+5
    elif (start <= 66):
        if (end <= 17):
            t = abs((end-(start-33)))+5
            dist = sqrt(576+(t*t))    
            dist = round(dist,2)      
        elif (end <= 33):
            t = abs(end-(start-33))
            dist = sqrt(576+(t*t))
            dist = round(dist,2)  
        elif (end <= 50):
            dist = abs((end-start))+5
        elif (end <= 66):
            dist = abs(end - start)
    dist = dist*20.9
    dist = round(dist,2)
    return float(str(round(dist,2)))

def csv_to_lists(r,data):
    list = []
    for i in range(r[0],r[1]):
        a = data[i]
        list.append(a)
    return list

#######################################################################
# Discards BGA components
#######################################################################
def discard_comp(import_table,Compdata_table):
    discard = []
    footprints = []
    for i in range(1,len(Compdata_table)):
        footprints.append(Compdata_table[i][0])
        
    for i in range(1,len(import_table)):
        if import_table[i][1] == "BGA484C80P22X22_1900X1900X190" or import_table[i][1] == "BGA96C80P16X9_1400X900X120":
            print_t("Discarded "+ import_table[i][1])
            discard.append(i)

    for i in range(len(discard)):    
        import_table.remove(import_table[discard[i]])
    return import_table

#######################################################################
# Creates a list (comp_freq) of unique components and how many of each
# there are in the import file.
#######################################################################
def component_frequency(import_table):
    comp_freq = []
    done = []
    temp = [0,0]
    for j in range(1,len(import_table)):
        if j not in done:
            temp[0] = import_table[j][1]
            temp[1] = import_table[j][10]
            count = 0
            to_append = []
            to_append.append(count)
            to_append.append(0)
            for i in range(j,len(import_table)):
                if ((temp[0] == import_table[i][1]) & (temp[1] == import_table[i][10])):
                    count = count + 1
                    to_append.append(i)
                    done.append(i)
            to_append[0] = count
            comp_freq.append(to_append)
    comp_freq.sort(key=lambda x:x[0],reverse=True)
    return comp_freq

#######################################################################
# Checks if the current nozzle is the correct nozzle to pick up the
# components by comparing it to data from Footprint_Library.csv.
#######################################################################
def nozzle_match(N_table,Footprint_Nozzle,nozzle,designator,import_table):

    N_type = N_table[nozzle][2]
    footprint_current = import_table[designator][1] # footprint of the input component
    col = Footprint_Nozzle[0].index(footprint_current)
    nozzle_current = Footprint_Nozzle[1][col] # list of all compatible parts with the chosen nozzle
    if nozzle_current == N_type:
        return True
    return False

#######################################################################
# Returns total number of components.
#######################################################################
def total_components(comp_freq):
    comp_total = 0
    for i in range(len(comp_freq)):
        comp_total = comp_total + comp_freq[i][0]
    return comp_total

#######################################################################
# Checks is the current nozzle can reach the current feeder
#######################################################################
def nozzle_reach(f,n):
    if ((n == 1) and (((f > 26) and (f < 34)) or (f > 59))):
        return False
    elif ((n == 2) and (((f > 27) and (f < 34)) or (f > 60) or (f < 2) or ((f > 33) and (f < 35)))):
        return False
    elif ((n == 3) and (((f > 28) and (f < 34)) or (f > 61) or (f < 3) or ((f > 33) and (f < 36)))):
        return False
    elif ((n == 4) and (((f > 29) and (f < 34)) or (f > 62) or (f < 4) or ((f > 33) and (f < 37)))):
        return False
    elif ((n == 5) and (((f > 30) and (f < 34)) or (f > 63) or (f < 5) or ((f > 33) and (f < 38)))):
        return False
    elif ((n == 6) and (((f > 31) and (f < 34)) or (f > 64) or (f < 6) or ((f > 33) and (f < 39)))):
        return False
    elif ((n == 7) and (((f > 32) and (f < 34)) or (f > 65) or (f < 7) or ((f > 33) and (f < 40)))):
        return False
    elif ((n == 8) and ((f < 8) or ((f > 33) and (f < 41)))):
        return False
    else:
        return True

#######################################################################
# Assigns each unique component to each feeder.
# checks if there is not feeder and nozzle mismatch and moves them
# checks for any microSD components and moves them to an empty feeder
# with no adjacent used feeders.
#######################################################################
def comp_feeder_learner(comp_freq_original,import_table,N_table,comp_total,Footprint_Nozzle):
    comp_freq = comp_freq_original

    mapping_start = [16,15,14,17,13,12,11]
    mapping_original = [18,19,20,21,22,23,24,25,50,51,49,52,48,53,47,54,46,55,45,56,44,57,43,58,10,
    9,26,8,27,7,28,6,29,5,30,4,31,3,32,2,33,1,42,59,41,60,40,61,39,62,38,63,37,64,36,65,35,66,34]

    mapping = []
    for i in range(len(comp_freq)):
        mapping.append(mapping_original[i])

    feeder_used = []
    current_feeder = 10
    current_comp = 0
    current_comp_feeder = 0
    current_comp_footprint = 0
    current_comp_nozzle = 0
    counter = 0
    checker = 0
    checker2 = 0
    N_types = []
    microsd = []
    micro = 0
    CN750 = []
    bool = 1
    loop = 0
    j = 0

    for i in range(len(mapping_start)):
        map = mapping_start[i]       # pick random feeder from list
        f_index = comp_freq[i][2]
        footprint = import_table[f_index][1]

        if(footprint != "MicroSD_-_DM3C-SF"):
            comp_freq[i][1] = map
            micro = 1
        if(comp_freq[i][1] != 0):
            feeder_used.append(comp_freq[i][1])

    for i in range(len(mapping_start),len(comp_freq)):

        map = random.choice(mapping)        # pick random feeder from list
        mapping.remove(map)                 # remove picked feeder to avoid duplicates
        f_index = comp_freq[i][2]
        footprint = import_table[f_index][1]

        if(footprint != "MicroSD_-_DM3C-SF"):
            comp_freq[i][1] = map
            micro = 1
        if(comp_freq[i][1] != 0):
            feeder_used.append(comp_freq[i][1])

    for i in range(len(comp_freq)):
        N_types = []
        counter = 0
        checker = 0
        if comp_freq[i][1] != 0:
            current_comp = comp_freq[i][2]
            current_comp_feeder = comp_freq[i][1]
            current_comp_footprint = import_table[current_comp][1]
            index = Footprint_Nozzle[0].index(current_comp_footprint)
            current_comp_nozzle = Footprint_Nozzle[1][index]
            for j in range(len(N_table)):
                if N_table[j][2] == current_comp_nozzle:
                    N_types.append(N_table[j][1])
            for j in range(len(N_types)):
                if (nozzle_reach(current_comp_feeder,int(N_types[j])) is True):
                    checker = 1
                    break          
            while ((checker == 0) and (checker2 == 0)):
                current_comp_feeder = (current_comp_feeder % 66) + 1
                counter += 1
                if (current_comp_feeder not in feeder_used):
                    for l in range(len(N_types)):
                        if (nozzle_reach(current_feeder,int(N_types[l])) is True): 
                            comp_freq[i][1] = current_comp_feeder
                            checker2 = 1
                if(counter > 67):
                    print_t("Too many components. Results may be Inaccurate.")
                    break

    if micro == 1:
        for i in range(len(N_table)):
            if N_table[i][2] == "CN750":
                CN750.append(N_table[i][1])
        for i in range(len(comp_freq)):
            while comp_freq[i][1] == 0:
                loop += 1
                if (current_feeder not in feeder_used) and ((current_feeder-1) not in feeder_used) and ((current_feeder+1) not in feeder_used):
                    for j in range(len(CN750)):
                        if (nozzle_reach(current_feeder,int(CN750[j])) is not True):
                            current_feeder += 1
                            bool = 0
                    if bool == 1:
                        comp_freq[i][1] = current_feeder
                        current_feeder = 1
                    bool = 1
                else:
                    if(current_feeder >= 66):
                        current_feeder = 1
                    elif(current_feeder < 66):
                        current_feeder += 1

                    if loop == 1000:
                        comp_freq.remove(comp_freq[i])
                        print_t("Discarded MicroSD_-_DM3C-SF")
                        comp_total = comp_total - 1
                        return comp_freq,comp_total
                             
    return comp_freq,comp_total

# def comp_feeder_designation(comp_freq_original,import_table,N_table):
#     comp_freq = comp_freq_original
#     mapping = [17,18,16,19,15,20,14,21,13,22,12,23,11,24,10,25,50,51,49,52,48,53,47,54,46,55,45,56,44,57,43,58,
#     9,26,8,27,7,28,6,29,5,30,4,31,3,32,2,33,1,42,59,41,60,40,61,39,62,38,63,37,64,36,65,35,66,34]
#     feeder_used = []
#     current_feeder = 9
#     microsd = []
#     micro = 0
#     CN750 = []
#     bool = 1
#     j = 0

#     for i in range(len(comp_freq)):

#         map = mapping[i]
#         f_index = comp_freq[i][2]
#         footprint = import_table[f_index][1]
#         if(footprint != "MicroSD_-_DM3C-SF"):
#             comp_freq[i][1] = map
#             micro = 1
#         if(comp_freq[i][1] != 0):
#             feeder_used.append(comp_freq[i][1])

#     if micro == 1:
#         for i in range(len(N_table)):
#             if N_table[i][2] == "CN750":
#                 CN750.append(N_table[i][1])
#         for i in range(len(comp_freq)):
#             while comp_freq[i][1] == 0:
#                 if (current_feeder not in feeder_used) and ((current_feeder-1) not in feeder_used) and ((current_feeder+1) not in feeder_used):
#                     for j in range(len(CN750)):
#                         if (nozzle_reach(current_feeder,int(CN750[j])) is not True):
#                             current_feeder += 1
#                             bool = 0
#                     if bool == 1:
#                         comp_freq[i][1] = current_feeder
#                         current_feeder = 1
#                     bool = 1
                    
#                 else:
#                     if(current_feeder >= 66):
#                         current_feeder += 1
#                     else:
#                         exit("Nozzle and Feeder Mismatch!")
                             
#     return comp_freq    

#######################################################################
# Assigns the picking order of nozzles for each feeder
#######################################################################
def comp_nozzle_designation(comp_total,new_comp,import_table):
    nozzle_amount = 8
    current_nozzle = 1
    left_bottom = 17
    right_bottom = 18
    left_top = 50
    right_top = 51
    comp_total_temp = comp_total
    prev_feeder = 0
    current_feeder = (left_bottom - nozzle_amount) + 1
    new_feeders = []
    nozzle_designation = []
    feeder_loop = 0
    stuck_loop = 0

    for i in range(len(new_comp)):
        new_feeders.append(new_comp[i][1])
    
    while comp_total > 0:
        
        temp_list = []
        if current_feeder in new_feeders:
            index = new_feeders.index(current_feeder)
                        
            if int(new_comp[index][0]) > 0:
                designator = int(new_comp[index][2])
                if ((nozzle_reach(current_feeder,current_nozzle) is not True) or (nozzle_match(N_table,Footprint_Nozzle,current_nozzle,designator,import_table) is not True)):
                    pass
                else:
                    stuck_loop = 0
                    feeder_loop = 0
                    new_comp[index][0] = int(new_comp[index][0]) - 1
                    temp_list = [new_comp[index][1],new_comp[index][2],current_nozzle]

                    if len(new_comp[index]) > 2:
                        del new_comp[index][2]

                    nozzle_designation.append(temp_list)

                    comp_total = comp_total - 1 

                    prev_feeder = current_feeder
                    if current_nozzle < nozzle_amount:
                        current_nozzle = current_nozzle + 1
                    elif current_nozzle == nozzle_amount:
                        current_nozzle = 1
                        current_feeder = 10
                        continue
            
        if current_feeder == 9:
            current_feeder = 34
        elif current_feeder == 25:
            current_feeder = 43
        elif current_feeder == 58:
            current_feeder = 1
        elif current_feeder == 42:
            current_feeder = 26
        elif current_feeder == 33:
            current_feeder = 59
        elif current_feeder == 66:
            current_feeder = 10
        else:
            current_feeder = current_feeder + 1
        if feeder_loop > 66:
            if current_nozzle < nozzle_amount:
                current_nozzle = current_nozzle + 1
            elif current_nozzle == nozzle_amount:
                current_nozzle = 1
            feeder_loop = 0
        feeder_loop = feeder_loop + 1
        stuck_loop = stuck_loop + 1

        if stuck_loop > 5000:
            # print("s")
            return nozzle_designation
    
    return nozzle_designation

#######################################################################
# update the starting feeder for measuring distance
#######################################################################
def update_distance_starting_position(nid,fid_prev,nid_prev):
    if fid_prev > 0:
        if nid > nid_prev:
            fid_prev = fid_prev + (abs(nid-nid_prev))
        elif nid < nid_prev:
            fid_prev = fid_prev - (abs(nid-nid_prev))
        elif nid == nid_prev:
            pass
    return fid_prev

#######################################################################
# Runs distance calculations across all the assigned feeders and nozzles
#######################################################################
def total_distance_calc(nozzle_designation):
    filled_nozzle = []
    distance = 0
    fid_prev = 0
    nid_prev = 0
    for i in range(len(nozzle_designation)):
        nid = nozzle_designation[i][2]
        filled_nozzle.append(nid)
        cid = nozzle_designation[i][1]
        fid = nozzle_designation[i][0]
        # Check if we need to move back to the center
        if i > 0:
            if nid < nid_prev:
                fid_prev = 0
                distance = distance + distance_calc(fid_prev,fid)

        # Moving to next feeder
        fid_prev = update_distance_starting_position(nid,fid_prev,nid_prev)
        distance = distance + distance_calc(fid_prev,fid)
        nid_prev = nid
        fid_prev = fid

    # last loop to move nozzles back to the center
    distance = distance + distance_calc(fid_prev,fid)
    return distance

#######################################################################
# Returns feeder data in the required format
#######################################################################
def feeder_output(comp_freq,F_table,Compdata_table,import_table):
    feeder_store = []
    
    for i in range(len(comp_freq)):
        f_index = comp_freq[i][1]
        c = comp_freq[i][2]
        for j in range(1,len(Compdata_table)):
            if ((Compdata_table[j][0] == import_table[c][1]) and (Compdata_table[j][1] == import_table[c][10])):
                c_index = j
        to_append = []
        for j in range(6):
            to_append.append(F_table[f_index][j])
        to_append.append(Compdata_table[c_index][0])
        to_append.append(Compdata_table[c_index][1])
        to_append.append(F_table[f_index][6])
        for j in range(2,len(Compdata_table[c_index])):
            to_append.append(Compdata_table[c_index][j])
        feeder_store.append(to_append)

    feeder_store.sort(key=lambda x:x[1],reverse=False)
    
    return feeder_store

#######################################################################
# Returns component data in the required format
#######################################################################
def comp_output(import_table,nozzle_designation):
    header = ['#Comp','Feeder ID','Comment','Footprint','Designatior','NozzleNumber','Pos X','Pos Y','Angle','Skip','Position']
    comp_header = []
    comp_header.append(header)
    for i in range(0,len(nozzle_designation)):
        n = nozzle_designation[i]
        append_list = []
        append_list.append('Comp')
        append_list.append(n[0])
        append_list.append(import_table[n[1]][10])
        append_list.append(import_table[n[1]][1])
        append_list.append(import_table[n[1]][0])
        append_list.append(n[2])
        append_list.append(import_table[n[1]][2])
        append_list.append(import_table[n[1]][3])
        append_list.append(import_table[n[1]][9])
        append_list.append('No')
        append_list.append('Align')   
        comp_header.append(append_list)
    return comp_header

#######################################################################
# Creates the output csv file
#######################################################################
def full_output(feeder_store,PCB_table,P_table,N_table,M_table,comp_store,sourcefile,sourcefile_import):
    header = ['#Feeder','Feeder ID','Skip','Pos X','Pos Y','Angle','Footprint','Comment','Nozzle','Pick Height','Pick Delay','Move Speed','Place Height','Place Delay','Place Speed','Accuracy',
              'Width','Length','Thickness','Size Analyze','Tray X','Tray Y','Columns','Rows','Right Top X','Right Top Y','Vision Model','Brightness','Vision Error','Vision Flash','Feeder Type','NoisyPoint']
    pre, ext = os.path.splitext(sourcefile_import)
    output = new_files +"/" + pre + "_out" + ext
    outp = pre + "_out" + ext
    with open(output, 'w') as f:
        converted_list = [str(element) for element in header]
        joined_list = ",".join(converted_list)
        f.write(joined_list)
        f.write('\n')          
        for line in feeder_store:
            converted_list = [str(element) for element in line]
            joined_list = ",".join(converted_list)
            f.write(joined_list)
            f.write('\n')   
        f.write('\n')  
        for line in PCB_table:
            converted_list = [str(element) for element in line]
            joined_list = ",".join(converted_list)
            f.write(joined_list)
            f.write('\n')   
        f.write('\n')  
        for line in P_table:
            converted_list = [str(element) for element in line]
            joined_list = ",".join(converted_list)
            f.write(joined_list)
            f.write('\n')  
        f.write('\n')   
        for line in N_table:
            converted_list = [str(element) for element in line]
            joined_list = ",".join(converted_list)
            f.write(joined_list)
            f.write('\n')   
        f.write('\n')  
        for line in M_table:
            converted_list = [str(element) for element in line]
            joined_list = ",".join(converted_list)
            f.write(joined_list)
            f.write('\n')  
        f.write('\n')           
        for line in comp_store:
            converted_list = [str(element) for element in line]
            joined_list = ",".join(converted_list)
            f.write(joined_list)
            f.write('\n')        
    return outp  

#######################################################################
# Runs the above functions 10000 times and picks the output with
# the shortest distance traveled.
#######################################################################
def shortest_distance(import_table,sourcefile,sourcefile_import,Compdata_table,M_table,N_table,P_table,PCB_table):
    sort_comparison_list = []
    new_comp_store = []
    total_distance = 100000
    prev_total_distance = total_distance
    loops = 0
    i = 0
    while i < RUNS:
        import_table = discard_comp(import_table,Compdata_table)
        comp_freq = component_frequency(import_table)
        new_comp_store.append(comp_freq)
        comp_total = total_components(comp_freq)
        new_comp,comp_total = comp_feeder_learner(comp_freq,import_table,N_table,comp_total,Footprint_Nozzle)

        temp_comp = new_comp
        feeder_store = feeder_output(new_comp,F_table,Compdata_table,import_table)

        nozzle_designation = comp_nozzle_designation(comp_total,new_comp,import_table)
        
        total_distance = total_distance_calc(nozzle_designation)
        if int(total_distance) < int(prev_total_distance):
            prev_total_distance = total_distance

            sort_comp = []
            sort_comp.append(temp_comp)
            sort_comp.append(total_distance)
            sort_comp.append(nozzle_designation)
            sort_comparison_list.append(sort_comp)
        i = i+1
        
        loops = loops+1

    sort_comparison_list.sort(key=lambda x:x[1],reverse=False)

    comp_store = comp_output(import_table,sort_comparison_list[0][2])
    output = full_output(feeder_store,PCB_table,P_table,N_table,M_table,comp_store,sourcefile,sourcefile_import)
    
    return sort_comparison_list[0][2],output

#######################################################################
# Same as shortest_distance() but modified for pre-made import files
#######################################################################
def shortest_distance_pre(import_table,sourcefile,sourcefile_import,Compdata_table,M_table,N_table,P_table,PCB_table):
    sort_comparison_list = []
    new_comp_store = []
    total_distance = 100000
    prev_total_distance = total_distance
    loops = 0
    i = 0
    while i < RUNS:
        import_table = discard_comp(import_table,Compdata_table)
        comp_freq = component_frequency(import_table)
        new_comp_store.append(comp_freq)
        comp_total = total_components(comp_freq)
        new_comp,comp_total = comp_feeder_learner(comp_freq,import_table,N_table,comp_total,Footprint_Nozzle)

        temp_comp = new_comp
        feeder_store = feeder_output(new_comp,F_table,Compdata_table,import_table)

        nozzle_designation = comp_nozzle_designation(comp_total,new_comp,import_table)
        
        total_distance = total_distance_calc(nozzle_designation)
        if int(total_distance) < int(prev_total_distance):
            prev_total_distance = total_distance

            sort_comp = []
            sort_comp.append(temp_comp)
            sort_comp.append(total_distance)
            sort_comp.append(nozzle_designation)
            sort_comparison_list.append(sort_comp)
        i = i+1
        
        loops = loops+1

    sort_comparison_list.sort(key=lambda x:x[1],reverse=False)

    comp_store = comp_output(import_table,sort_comparison_list[0][2])
    output = full_output(feeder_store,PCB_table,P_table,N_table,M_table,comp_store,sourcefile,sourcefile_import)
    
    return sort_comparison_list[0][2],output


##############################################################################################################################################
# SIMULATION
##############################################################################################################################################
outline = "#000"
fill = "#ffe"

#######################################################################
# Update the feeder nozzle and component counters. components 
# uses the footprint from import_table
#######################################################################
def update_counters(import_table,canvas,fid,nid,cid,canvas_counters,reset):
    if reset:
        canvas.itemconfig(canvas_counters[1], text="0")
        canvas.itemconfig(canvas_counters[2], text="0")
        canvas.itemconfig(canvas_counters[3], text="none") 
        return
    cid_footprint = import_table[cid][1]
    canvas.itemconfig(canvas_counters[1], text=str(fid))
    canvas.itemconfig(canvas_counters[2], text=str(nid))
    canvas.itemconfig(canvas_counters[3], text=str(cid_footprint))

def update_distance(canvas,distance,canvas_counters):
    d = distance
    d = round(d,2)
    canvas.itemconfig(canvas_counters[0], text=str(d)+" mm")

def update_remaining_feeders(canvas,fid,remaining_feeders,feeder_canvas):
    if int(fid) in remaining_feeders:
        canvas.itemconfig(feeder_canvas[fid], fill='yellow')
    elif int(fid) not in remaining_feeders:
        canvas.itemconfig(feeder_canvas[fid], fill=fill)

def update_distance_starting_position(nid,fid_prev,nid_prev):
    if fid_prev > 0:
        if nid > nid_prev:
            fid_prev = fid_prev + (abs(nid-nid_prev))
        elif nid < nid_prev:
            fid_prev = fid_prev - (abs(nid-nid_prev))
        elif nid == nid_prev:
            pass
    return fid_prev
    

#######################################################################
# Moves all 8 nozzles to (x_move,y_move). id is the number of nozzle
# picking up.
#######################################################################
def animate_moveto(canvas,nozzle_canvas,id,n_c,x_move, y_move):
    x = x_move
    y = y_move
    for i in range(id,len(n_c)):
        canvas.moveto(n_c[i],x,y)
        x = x + 23
    x = x_move
    for i in range(id-1,0,-1):
        x = x - 23
        canvas.moveto(nozzle_canvas[i],x,y)


#######################################################################
# Module to animate the nozzles picking up up the components for the
# feeders based on their nozzle_designation
#######################################################################
def nozzle_animation(nozzle_designation,import_table):

    # Creating tkinter canvas and drawing all objects (feeder, nozzle, pcb, counters)
    ws = tk.Tk()
    ws.title('K1830 Simulation')
    ws.geometry('1000x600')
    ws.config(bg='#345')

    canvas = Canvas(
        ws,
        height=600,
        width=1000,
        bg="#ddd"
        )

    canvas.pack()

    feeder_canvas = [0]
    nozzle_canvas = [0]
    x0 = 50
    x1 = x0 + 18
    y0 = 500
    y1 = y0 - 60

    def draw_nozzles(start,end,x0, y0, x1, y1, nozzle_canvas):
        for i in range(start,end):
            n = canvas.create_oval(x0, y0, x1, y1, outline=outline, fill=fill)
            data = [n,x0,y0,x1,y1]
            nozzle_canvas.append(n)
            x0 = x0 + 23
            x1 = x0 + 18
        return nozzle_canvas

    def draw_feeders(start,end,x0, y0, x1, y1, feeder_canvas):
        st_x0 = x0
        st_x1 = x1
        for i in range(start,end):
            f  = canvas.create_rectangle(x0, y0, x1, y1, outline=outline, fill=fill)
            data = [f,x0,y0,x1,y1]
            feeder_canvas.append(f)
            x0 = x0 + 23
            x1 = x0 + 18
        return x0, y0, x1, y1, feeder_canvas

    def draw_feeders_label(start,end,x0, y0, x1, y1):
        for i in range(start,end):
            if i >= 34:
                canvas.create_text((x0+9, y0-10), text=str(i))
            else:
                canvas.create_text((x0+9, y0-50), text=str(i))
            x0 = x0 + 23
            x1 = x0 + 18
        return x0, y0, x1, y1

    def pause_sim(pause_keyboard,RUN_or_PAUSE):
        canvas.itemconfig(RUN_or_PAUSE, text="Press 'r' to RUN")
        canvas.update()
        canvas.after(50)
        while pause_keyboard == True:
            if keyboard.is_pressed('r'):
                pause_keyboard = False
        canvas.itemconfig(RUN_or_PAUSE, text="Press 'p' to PAUSE") 
        return pause_keyboard

    x0, y0, x1, y1, feeder_canvas = draw_feeders(1,18,x0, y0, x1, y1, feeder_canvas)

    x0 = x0 + 150
    x1 = x0 + 18
    x0, y0, x1, y1, feeder_canvas = draw_feeders(18,34,x0, y0, x1, y1, feeder_canvas)

    x0 = 50
    x1 = x0 + 18
    y0 = 150
    y1 = y0 - 60
    x0, y0, x1, y1, feeder_canvas = draw_feeders(34,51,x0, y0, x1, y1, feeder_canvas)

    x0 = x0 + 150
    x1 = x0 + 18
    x0, y0, x1, y1, feeder_canvas = draw_feeders(51,67,x0, y0, x1, y1, feeder_canvas)

    x0 = 50
    x1 = x0 + 18
    y0 = 500
    y1 = y0 - 60
    x0, y0, x1, y1 = draw_feeders_label(1,18,x0, y0, x1, y1)

    x0 = x0 + 150
    x1 = x0 + 18
    x0, y0, x1, y1 = draw_feeders_label(18,34,x0, y0, x1, y1)

    x0 = 50
    x1 = x0 + 18
    y0 = 150
    y1 = y0 - 60
    x0, y0, x1, y1 = draw_feeders_label(34,51,x0, y0, x1, y1)

    x0 = x0 + 150
    x1 = x0 + 18
    x0, y0, x1, y1 = draw_feeders_label(51,67,x0, y0, x1, y1)

    x0 = 425
    x1 = x0 + 18
    y0 = 280
    y1 = y0 + 18
    nozzle_canvas = draw_nozzles(1,9,x0, y0, x1, y1, nozzle_canvas)

    x0 = 180
    y0_text = 550
    canvas.create_text(x0,y0_text,fill="black",font="Arial 12 bold",
                            text="Total Distance:")
    counter_d = canvas.create_text(x0+65,y0_text,fill="black",font="Arial 12 bold",anchor="w",
                            text="0.00 mm")

    x0 = x0 + 340
    canvas.create_text(x0,y0_text,fill="black",font="Arial 12 bold",
                            text="Feeder: ")
    counter_f = canvas.create_text(x0+35,y0_text,fill="black",font="Arial 12 bold",anchor="w",
                            text="0")

    x0 = x0 + 120
    canvas.create_text(x0,y0_text,fill="black",font="Arial 12 bold",
                            text="Nozzle: ")
    counter_n = canvas.create_text(x0+35,y0_text,fill="black",font="Arial 12 bold",anchor="w",
                            text="0")

    x0 = x0 + 120
    canvas.create_text(x0,y0_text,fill="black",font="Arial 12 bold",
                            text="Comp: ")
    counter_c = canvas.create_text(x0+35,y0_text,fill="black",font="Arial 12 bold",anchor="w",
                            text="none")

    canvas_counters = [counter_d,counter_f,counter_n,counter_c]

    RUN_or_PAUSE = canvas.create_text(835,30,fill="black",font="Arial 12 bold",text="Press 'p' to PAUSE")

    remaining_feeders = []
    for i in range(len(nozzle_designation)):
        remaining_feeders.append(nozzle_designation[i][0])
        canvas.itemconfig(feeder_canvas[nozzle_designation[i][0]], fill='yellow')
    filled_nozzle = []
    distance = 0
    fid_prev = 0
    nid_prev = 0
    pause_keyboard = False
    canvas.update()
    canvas.after(2000)
    for i in range(len(nozzle_designation)):
        if keyboard.is_pressed('p'):
            pause_keyboard = True 
            canvas.update()
            canvas.after(30)
        nid = nozzle_designation[i][2]
        filled_nozzle.append(nid)
        cid = nozzle_designation[i][1]
        fid = nozzle_designation[i][0]
        # Check if we need to move back to the center
        if i > 0:
            if nid < nid_prev:
                fid_prev = 0
                if keyboard.is_pressed('p'):
                    pause_keyboard = True 
                    canvas.update()
                    canvas.after(30)              
                distance = distance + distance_calc(fid_prev,fid)
                update_distance(canvas,distance,canvas_counters)
                for j in range(len(filled_nozzle)):
                    fnid = filled_nozzle[j]
                    canvas.itemconfig(nozzle_canvas[fnid], fill='green')
                x0,y0 = 425,280
                animate_moveto(canvas,nozzle_canvas,1,nozzle_canvas,x0, y0)
                canvas.update()
                canvas.after(300) 
                for j in range(len(filled_nozzle)-1):
                    fnid = filled_nozzle[j]
                    canvas.itemconfig(nozzle_canvas[fnid], fill=fill)
                filled_nozzle = [nid]

        # Moving to next feeder
        x0,y0,x1,y1 = canvas.coords(feeder_canvas[fid])
        if fid >= 34:
            y0 = y1 + 5
        else:
            y0 = y0 - 25
        fid_prev = update_distance_starting_position(nid,fid_prev,nid_prev)
        update_counters(import_table,canvas,fid,nid,cid,canvas_counters,0)
        distance = distance + distance_calc(fid_prev,fid)
        update_distance(canvas,distance,canvas_counters)
        canvas.itemconfig(nozzle_canvas[nid], fill='green')
        canvas.itemconfig(feeder_canvas[fid], fill='green')
        animate_moveto(canvas,nozzle_canvas,nid,nozzle_canvas,x0, y0)
        if pause_keyboard == True:
            pause_keyboard = pause_sim(pause_keyboard,RUN_or_PAUSE)
        canvas.update()
        canvas.after(300)
        canvas.itemconfig(nozzle_canvas[nid], fill=fill)
        remaining_feeders.pop(0)
        update_remaining_feeders(canvas,fid,remaining_feeders,feeder_canvas)

        # canvas.itemconfig(feeder_canvas[fid], fill=fill)
        nid_prev = nid
        fid_prev = fid


    # last loop to move nozzles back to the center
    for j in range(len(filled_nozzle)):
        fnid = filled_nozzle[j]
        canvas.itemconfig(nozzle_canvas[fnid], fill='green')
    x0,y0 = 425,280
    animate_moveto(canvas,nozzle_canvas,1,nozzle_canvas,x0, y0)
    canvas.update()
    canvas.after(700)   
    for j in range(len(filled_nozzle)):
        fnid = filled_nozzle[j]
        canvas.itemconfig(nozzle_canvas[fnid], fill=fill)
    filled_nozzle = []    
    update_counters(import_table,canvas,fid,nid,cid,canvas_counters,1)
    distance = distance + distance_calc(fid_prev,fid)
    update_distance(canvas,distance,canvas_counters)
    print_t("Simulation Complete")
    ws.mainloop()


##############################################################################################################################################
# USER INTERFACE
##############################################################################################################################################
window = tk.Tk()

text = tk.Text(window)
text.pack()
text.place(x=30,y=325,height=210,width=615)

# Basic setup of window
window.title("K1830 Pick and Place")
window.geometry("680x550")
window.resizable(False, False)

# Text in the window
label1 = Label(window,
               text="Choose a File",
               font=("Arial bold", 22),
               )
label1.place(x=30,y=30)

# Showing files in the folder
file_view = tk.Listbox(window,width=42,height= 9,font=(11))
file_view.place(x=30,y=80)

for items in os.listdir(import_file_location):
    if items.endswith(".csv"):      # Only shows csv files
        file_view.insert(0, items)

# Function to run the optimization from pre-existing import file
def run_program_pre(sourcefile,sourcefile_import,import_table,Compdata_table,M_table,N_table,P_table,PCB_table):
    nozzle_designation,output = shortest_distance_pre(import_table,sourcefile,sourcefile_import,Compdata_table,M_table,N_table,P_table,PCB_table)
    return nozzle_designation, import_table, output

# Function to run the optimization from import file
def run_program(sourcefile,sourcefile_import,import_table,Compdata_table,M_table,N_table,P_table,PCB_table):
    import_table = list(csv.reader(open(sourcefile)))
    import_table = Check_footprints_comments(import_table,Compdata_table)
    nozzle_designation,output = shortest_distance(import_table,sourcefile,sourcefile_import,Compdata_table,M_table,N_table,P_table,PCB_table)
    return nozzle_designation, import_table, output

# Function for storing the selected listbox value and then runs run_program
def selected_item(Compdata_table,M_table,N_table,P_table,PCB_table):
    sourcefile = ''
    for i in file_view.curselection():
        sourcefile = "Import/" + file_view.get(i)
        sourcefile_import = file_view.get(i)
    if sourcefile == '':
        print_t("Please Select a CSV file.")
        return
    table_check = list(csv.reader(open(sourcefile)))
    if table_check[0][0] == "#Feeder":
        Compdata_table,M_table,N_table,P_table,PCB_table = [],[],[],[],[]
        import_table,Compdata_table,M_table,N_table,P_table,PCB_table = Existing_Table(table_check,Compdata_table,M_table,N_table,P_table,PCB_table)
        print_t("Running optimization on '" + sourcefile_import + "'")
        window.update()
        window.after(20) 
        x,y,output = run_program_pre(sourcefile,sourcefile_import,import_table,Compdata_table,M_table,N_table,P_table,PCB_table)
        print_t("Done. Result '" + output + "' stored in Output folder")

    elif table_check[0][0] != "Designator":
        print_t(sourcefile_import + " is not in the correct format.")
        return
    else:
        print_t("Running optimization on '" + sourcefile_import + "'")
        window.update()
        window.after(20) 
        N_table = Nozzle_Suggest(table_check,Footprint_Library_table,N_table)
        x,y,output = run_program(sourcefile,sourcefile_import,table_check,Compdata_table,M_table,N_table,P_table,PCB_table)
        print_t("Done. Result '" + output + "' stored in Output folder")

# Function for storing the selected listbox value and then runs run_simulation
def selected_item_sim(Compdata_table,M_table,N_table,P_table,PCB_table):
    sourcefile = ''
    for i in file_view.curselection():
        sourcefile = "Import/" + file_view.get(i)
        sourcefile_import = file_view.get(i)
    if sourcefile == '':
        print_t("Please Select a CSV file.")
        return
    table_check = list(csv.reader(open(sourcefile)))
    if table_check[0][0] == "#Feeder":
        Compdata_table,M_table,N_table,P_table,PCB_table = [],[],[],[],[]
        import_table,Compdata_table,M_table,N_table,P_table,PCB_table = Existing_Table(table_check,Compdata_table,M_table,N_table,P_table,PCB_table)
        print_t("Running Simulation on '" + sourcefile_import + "'")
        window.update()
        window.after(20) 
        nozzle_designation,import_table,x = run_program_pre(sourcefile,sourcefile_import,import_table,Compdata_table,M_table,N_table,P_table,PCB_table)
    elif table_check[0][0] != "Designator":
        print_t(sourcefile_import + " is not in the correct format.")
        return
    else:
        print_t("Running Simulation on '" + sourcefile_import + "'")
        window.update()
        window.after(20) 
        N_table = Nozzle_Suggest(table_check,Footprint_Library_table,N_table)
        nozzle_designation,import_table,x = run_program(sourcefile,sourcefile_import,table_check,Compdata_table,M_table,N_table,P_table,PCB_table)

    nozzle_animation(nozzle_designation,import_table)
    

# Exits the program
def Exit():
    sys.exit("Done")

img_run = PhotoImage(file = file_location + '/Images/Run.png')
img_run = img_run.zoom(10)
img_run = img_run.subsample(64)
button1 = tk.Button(window, text='Run Program',image = img_run,command=lambda: selected_item(Compdata_table,M_table,N_table,P_table,PCB_table))
button1.place(x=542,y=20)
button1_ttp = CreateToolTip(button1, \
    "Run Optimization")


img_sim = PhotoImage(file = file_location + '/Images/Sim.png')
img_sim = img_sim.zoom(10)
img_sim = img_sim.subsample(64)
button2 = tk.Button(window, text='Run Simulation',image = img_sim,command=lambda: selected_item_sim(Compdata_table,M_table,N_table,P_table,PCB_table))
button2.place(x=542,y=135)
button2_ttp = CreateToolTip(button2, \
    "Run Simulation")

img_exit = PhotoImage(file = file_location + '/images/Exit.png')
img_exit = img_exit.zoom(6)
img_exit = img_exit.subsample(64)
button3 = tk.Button(window, text='Exit',image = img_exit,command=lambda: Exit(),anchor=E)
button3.grid(row = 2, column = 6,sticky="ne",rowspan=4)
button3.place(x=580,y=250)
button3_ttp = CreateToolTip(button3, \
    "Exit")

# Defining infinite loop
window.mainloop()
