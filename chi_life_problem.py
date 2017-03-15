#1 Import csv, numpy, and matplotlib.plot
#2 Open the chi_life_expectancy.txt file
#3 Use csv.reader(file, delimeter='\t') to read in the file to a list.  Make appropriate lists for plotting. Community name will be the x and 2010 life expectancy on the y.
#4 Plot the life_expectancy_2010_list vs a numpy arange() as a bar graph
#5 Use ax = plt.gca() to grab the axes object as ax. Use ax.set_xticklabels(community_list) to place the labels on the x axis, use the kwarg rotation=60 to tilt the lettering since there are a lot of communities
#6  Set an appropriate plt.ylim([min,max])
#7  Label your axes
#8  Add a title
#9  Add text to indicate the minimum and maximum values
#10 Customize your graph in at least two other ways using documentation from matplotlib.org
#11  Comment your code as always.

# Note:  If you would like to present something different than the above for your graph using this dataset, just let me know your intentions before you start and I will do my best to support you.
import csv
import numpy as np
import matplotlib.pyplot as plt # we import libraries
file=open("chi_life_expectancy.txt","r")  # we open the file
life_list=[]    #make an empty list

reader= csv.reader(file, delimiter="\t")    #give instructions for splitting the text

for row in reader:      #split the text up
    life_list.append(row)
print(life_list)


community_area_number_list=[]
community_area_list=[]
life_expectancy_90=[]
lower_ci_90=[]
upper_ci_90=[]
life_expectancy_00=[]
lower_ci_00=[]
upper_ci_00=[]
life_expectancy_10=[]
lower_ci_10=[]
upper_ci_10=[]     # make empty list for all the information we have

for i in range (1,len(life_list)):
    community_area_number_list.append(life_list[i][0])
    community_area_list.append(life_list[i][1])
    life_expectancy_90.append(float(life_list[i][2]))
    lower_ci_90.append(life_list[i][3])
    upper_ci_90.append(life_list[i][4])
    life_expectancy_00.append(life_list[i][5])
    lower_ci_00.append(life_list[i][6])
    upper_ci_00.append(life_list[i][7])
    life_expectancy_10.append(life_list[i][8])
    lower_ci_10.append(life_list[i][9])
    upper_ci_10.append(life_list[i][10])      #fill up the lists

print(community_area_list)     #check if we have the correct information filled

plt.figure(figsize=[15,7], tight_layout=True)         #adjust width, height and text

plt.bar(np.arange(len(life_expectancy_90)),life_expectancy_90,color="blue",alpha=0.3)  #format the life expectancy list

plt.xticks(np.arange(len(life_expectancy_90)),life_expectancy_10)
plt.ylim(55,80)
plt.text(35,57,"minimum=57",color="red",fontsize=15)
plt.arrow(17,16.4,19.7,40,head_width=0.5,color="red")
plt.text(70,79,"maximum=79",color="red",fontsize=15)
plt.xlabel("Neighborhood")
plt.ylabel("Life Expectancy")
plt.title("Life Expectancy in Chicago",fontsize=25)
ax=plt.gca()
ax.set_xticklabels(community_area_list,rotation=90)     #add and rotate the text of the community area list




plt.show()

