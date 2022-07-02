import csv
from math import sqrt
import os
import random
from re import S
sourcefile = "DEMO_IMPORT.csv"
output = "demo_output_new.csv"

def distance_calc(start,end):
    dist = 0
    t = 0
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
    return dist
            
def distance_place(start):
    t = 0
    dist = 0
    if (start <= 17):
        t = abs(17-start)+2.5
        dist = sqrt(144+(t*t))
        dist = round(dist,2)
    elif (start <= 33):
        t = abs(33-start)+2.5
        dist = sqrt(144+(t*t))
        dist = round(dist,2)
    elif (start <= 50):
        t = abs(50-start)+2.5
        dist = sqrt(144+(t*t))
        dist = round(dist,2)
    elif (start <= 66):
        t = abs(66-start)+2.5
        dist = sqrt(144+(t*t))
        dist = round(dist,2)
    return dist

def csv_to_lists(r,data):
    list = []
    for i in range(r[0],r[1]):
        a = data[i]
        list.append(a)
    return list

import_table = list(csv.reader(open(sourcefile)))
print(import_table[0][1])

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

def total_components(comp_freq):
    comp_total = 0
    for i in range(len(comp_freq)):
        comp_total = comp_total + comp_freq[i][0]
    return comp_total

def comp_feeder_learner(comp_freq):
    # This list shows all possible feeders to pick out from
    feeders = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,
               36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66]
    for i in range(len(comp_freq)):
        mapping = random.choice(feeders)        # pick random feeder from list
        feeders.remove(mapping)                 # remove picked feeder to avoid duplicates
        j = 0
        map = mapping
        comp_freq[i][1] = map
        j = j + 1   
    return comp_freq    

def comp_feeder_designation(comp_freq):
    mapping = [17,18,16,19,15,20,14,21,13,22,12,23,11,24,10,25,50,51,49,52,48,53,47,54,46,55,45,56,44,57,43,58,
    9,26,8,27,7,28,6,29,5,30,4,31,3,32,2,33,1,42,59,41,60,40,61,39,62,38,63,37,64,36,65,35,66,34]
    # mapping = [42,39,34,40,18,54,44,61,41,9,30,11,25,14,20,58,22,19,10,36,51,47,56]
    # mapping = [64,18,16,19,15,20,14,21,13,22,12,23,11,24,10,25,50,51,49,52,48,53,47,54,46,55,45,56,44,57,43,58,
    # 9,26,8,27,7,28,6,29,5,30,4,31,3,32,2,33,1,42,59,41,60,40,61,39,62,38,63,37,64,36,65,35,17,34]
    j = 0
    for i in range(len(comp_freq)):
        map = mapping[j]
        comp_freq[i][1] = map
        j = j + 1   
    return comp_freq    

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

def comp_nozzle_designation(comp_total,new_comp):
    nozzle_amount = 8
    current_nozzle = 1
    left_bottom = 17
    right_bottom = 18
    left_top = 50
    right_top = 51
    total_travel_dist = 0
    comp_total_temp = comp_total
    prev_feeder = 0
    current_feeder = (left_bottom - nozzle_amount) + 1
    new_feeders = []
    nozzle_designation = []
    feeder_loop = 0

    for i in range(len(new_comp)):
        new_feeders.append(new_comp[i][1])
        
    # print("comp total =", comp_total)
    
    while comp_total > 0:
        
        temp_list = []
        if current_feeder in new_feeders:
            index = new_feeders.index(current_feeder)
                        
            if int(new_comp[index][0]) > 0:
                if (nozzle_reach(current_feeder,current_nozzle) is not True):
                    if feeder_loop == 66:
                        if current_nozzle < nozzle_amount:
                            current_nozzle = current_nozzle + 1
                        elif current_nozzle == nozzle_amount:
                            current_nozzle = 1
                        feeder_loop = 0
                    feeder_loop = feeder_loop + 1
                    continue
                else:
                    feeder_loop = 0
                    new_comp[index][0] = int(new_comp[index][0]) - 1
                    temp_list = [new_comp[index][1],new_comp[index][2],current_nozzle]

                    if len(new_comp[index]) > 2:
                        del new_comp[index][2]

                    nozzle_designation.append(temp_list)

                    comp_total = comp_total - 1 

                    if comp_total == 0:
                        total_travel_dist = total_travel_dist + distance_place(current_feeder)
                    elif current_nozzle == nozzle_amount:
                        total_travel_dist = total_travel_dist + distance_place(current_feeder)
                    elif current_nozzle == 1:
                        total_travel_dist = total_travel_dist + distance_place(current_feeder)
                    elif comp_total == (comp_total_temp - 1):
                        total_travel_dist = total_travel_dist + distance_place(current_feeder)
                    else:
                        total_travel_dist = total_travel_dist + distance_calc(prev_feeder,current_feeder+1)

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
 
    return nozzle_designation, total_travel_dist

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
 
    with open(output, 'w') as f:
        for line in comp_header:
            converted_list = [str(element) for element in line]
            # print(converted_list)
            joined_list = ",".join(converted_list)
            f.write(joined_list)
            f.write('\n')
       

comp_freq = component_frequency(import_table)
comp_total = total_components(comp_freq)
new_comp = comp_feeder_designation(comp_freq)

nozzle_designation, total_distance = comp_nozzle_designation(comp_total,new_comp)

def shortest_distance(import_table):
    sort_comparison_list = []
    new_comp_store = []
    for i in range(100):
        comp_freq = component_frequency(import_table)
        new_comp_store.append(comp_freq)
        comp_total = total_components(comp_freq)
        new_comp = comp_feeder_learner(comp_freq)

        temp_comp = new_comp

        nozzle_designation, total_distance = comp_nozzle_designation(comp_total,new_comp)
        sort_comp = []
        sort_comp.append(temp_comp)

        sort_comp.append(total_distance)
        sort_comp.append(nozzle_designation)
        sort_comparison_list.append(sort_comp)

    sort_comparison_list.sort(key=lambda x:x[1],reverse=False)
    for i in range(10):
        pass
        print("distance: ",sort_comparison_list[i][1])
        print()
        print("nozzles: ",sort_comparison_list[i][2])
        print()
        print()

# shortest_distance(import_table)
comp_output(import_table,nozzle_designation)
