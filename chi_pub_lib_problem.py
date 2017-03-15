
# MATPLOTLIB PROBLEM # 1
# Chicago Public Library Visitors by Month (25pts)
# open and read in the "chilib_visitors_2016" file into a list
# calculate (and make a list of) the total visitors to Chicago libraries each month.  Do not plot every library individually.  Find the total for all libraries and plot that.
# Additionally, add lines for the three most visited libraries.
# plot the total visitors on the y and month on the x.  You will have 4 separate lines (total and 3 libraries)
# add a legend
# label axes, title the graph
import csv
import numpy as np
import matplotlib.pyplot as plt
file2=open("chilib_visitors_2016","r")

ex_list = []
jan=0
feb=0
mar=0
apr=0
may=0
june=0
july=0
aug=0
sept=0
oct=0
nov=0
dec=0

reader = csv.reader(file2, delimiter="\t")

for row in reader:
    ex_list.append(row)
print(ex_list)

for i in range(1,len(ex_list)):
    jan+=int(ex_list[i][1])
    feb+=int(ex_list[i][2])
    mar+=int(ex_list[i][3])
    apr+=int(ex_list[i][4])
    may+=int(ex_list[i][5])
    june+=int(ex_list[i][6])
    july+=int(ex_list[i][7])
    aug+=int(ex_list[i][8])
    sept+=int(ex_list[i][9])
    oct+=int(ex_list[i][10])
    nov+=int(ex_list[i][11])
    dec+=int(ex_list[i][12])

month_list = [jan,feb,mar,apr,may,june,july,aug,sept,oct,nov,dec]

month_text=["January","February","March","April","May","June","July","August","September","October","November","December"]

most_suc=[]
numbers_list=[]
extra=[]
for i in range(1,len(ex_list)):
    x=0
    most_suc.append(ex_list[i][0])
    for y in range(1,len(ex_list[i])):
        x+=int(ex_list[i][y])
    numbers_list.append(x)

print(numbers_list)

full_list=[val for pair in zip(most_suc, numbers_list) for val in pair]
print(full_list)

full_list=[full_list[i:i + 2] for i in range(0, len(full_list), 2)]

def sorting(my_list):
    for pos in range(len(my_list)):
        min_pos = pos
        for scan_pos in range(min_pos, len(my_list)):
            if my_list[scan_pos][1] > my_list[min_pos][1]:
                min_pos = scan_pos
        temp = my_list[pos]
        my_list[pos] = my_list[min_pos]
        my_list[min_pos] = temp

    print(my_list)

sorting(full_list)

plt.figure(figsize=[15,7], tight_layout=True)

plt.plot(np.arange(len(month_list)),month_list,color="red")
plt.plot(np.arange(len(numbers_list),full_list[0][1]),color="blue")

plt.xticks(np.arange(len(month_list)),month_text)
plt.xticks(np.arange(len(numbers_list)),full_list[0][0])




plt.show()