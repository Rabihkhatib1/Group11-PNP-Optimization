from pandas import *
import csv
sourcefile = "Starfish_Top_v1.1.2.csv"

Feeder = [1,24]
pcb = [Feeder[1]+2,27]
Panel = [pcb[1]+2,32]
Nozzle = [Panel[1]+2,42]
Mark = [Nozzle[1]+2,46]
Comp = [Mark[1]+2,95]

Feeder_list = [[]*((Feeder[1]+1)-Feeder[0])]
pcb_list = [[]*((pcb[1]+1)-pcb[0])]
Panel_list = [[]*((Panel[1]+1)-Panel[0])]
Nozzle_list = [[]*((Nozzle[1]+1)-Nozzle[0])]
Mark_list = [[]*((Mark[1]+1)-Mark[0])]
Comp_list = [[]*((Comp[1]+1)-Comp[0])]

def csv_to_lists(r,data):
    list = []
    for i in range(r[0],r[1]):
        a = data[i]
        list.append(a)
    return list

df = read_csv(sourcefile)

# with open('test.txt', 'w') as f:
#     f.write(df.to_string())
# print(df)

data = list(csv.reader(open(sourcefile)))

Feeder_list = csv_to_lists(Feeder,data)
pcb_list = csv_to_lists(pcb,data)
Panel_list = csv_to_lists(Panel,data)
Nozzle_list = csv_to_lists(Nozzle,data)
Mark_list = csv_to_lists(Mark,data)
Comp_list = csv_to_lists(Comp,data)

# print("Feeder_list =", Feeder_list)
# print("pcb_list =", pcb_list)
# print("Panel_list =", Panel_list)
# print("Nozzle_list =", Nozzle_list)
# print("Mark_list =", Mark_list)
# print("Comp_list =", Comp_list)

def component_frequecy(feederid,footprints,comp_feederid,comp_footprint):
    comp_freq = [[0]*3 for x in range(len(feederid))]
    for i in range(len(feederid)):
        comp_freq[i][0] = feederid[i]
        comp_freq[i][1] = footprints[i]
        for j in range(len(comp_feederid)):
            if (comp_freq[i][0] == comp_feederid[j]):
                comp_freq[i][2] += 1
    comp_freq.sort(key=lambda x:x[2],reverse=True)
    return comp_freq

Feeder_list_feeder = []
Feeder_list_footprint = []
Comp_list_feeder = []
Comp_list_footprint = []

for i in range(len(Feeder_list)):
    x = Feeder_list[i][1]
    y = Feeder_list[i][6]
    Feeder_list_feeder.append(x)
    Feeder_list_footprint.append(y)

for i in range(len(Comp_list)):
    x = Comp_list[i][1]
    y = Comp_list[i][3]
    Comp_list_feeder.append(x)
    Comp_list_footprint.append(y)

comp_freq = component_frequecy(Feeder_list_feeder,Feeder_list_footprint,Comp_list_feeder,Comp_list_footprint)

# for i in range(len(comp_freq)):
#     print(comp_freq[i])

def comp_feeder_designation(comp_freq):
    mapping = [17,18,16,19,15,20,14,21,13,22,12,23,11,24,10,25,50,51,49,52,48,53,47,54,46,55,45,56,44,57,43,58,
    9,26,8,27,7,28,6,29,5,30,4,31,3,32,2,33,1,42,59,41,60,40,61,39,62,38,63,37,64,36,65,35,66,34]

    for i in range(len(comp_freq)):
        map = mapping[i]
        if int(comp_freq[i][0]) > 66:
            comp_freq[i].append(comp_freq[i][0]) 
        else:
            comp_freq[i].append(map)    
    return comp_freq

new_comp = comp_feeder_designation(comp_freq)

for i in range(len(new_comp)):
    print(new_comp[i])




