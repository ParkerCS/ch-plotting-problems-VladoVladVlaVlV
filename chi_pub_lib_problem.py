
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
print(month_list)
month_text=["January","February","March","April","May","June","July","August","September","October","November","December"]
print(month_text)
plt.figure(figsize=[15,7], tight_layout=True)

plt.plot(np.arange(len(month_list)),month_list,color="red")

plt.xticks(np.arange(len(month_list)),month_text)




plt.show()