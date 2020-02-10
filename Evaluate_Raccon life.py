#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Assignment 3, ABE651000

@author: gautam6
"""

#Reading a ASCII fine 
george=open("2008Male00006.txt","r")
#The open command accept two argument:first  says the file name and second tells python,r for read
lines=george.readlines() #read all the lines in the file
george.close()  #Close the file
data=[0]*(len(lines)-2) # create a matrix with 0
for lidx in range (len(lines[1:15])):            #Since 1st and last line can not be splited
    data[lidx]=lines[1:15][lidx].strip().split(",")  
    data[lidx][3:6]=map(float,data[lidx][3:6])
    data[lidx][8:15]=map(float,data[lidx][8:15])

raccon_death=lines[15].strip()  #The 15th row has the information of raccon status
data_header=lines[0].strip().split(",") # The 1st row is the header indicated by 0

dictionary= dict()    # Function dict creats a dictionary and is blank
datat=list(map(list,zip(*data)))  #Transposing the data matrix

for i in range(len(data_header)):   #Adds values from datat to header
    for i in range(len(datat)):
        dictionary[data_header[i]]=datat[i]
        
dictionary['Note']=raccon_death  #Adding notes about raccon's death status
def sum_list(a):   # defining a function to calculate sum of list
    sum_a=sum(a)
    return round(sum_a,2)  #Rounding of the result at a 2 decimal degit

def average_list(a):   #Defining a function to caluclate the average of list
    return sum(a)/len(a)

import math

def distance(x1,x2,y1,y2):  # Defining a function to calculate the distance between two points
    dis= math.sqrt((x2-x1)**2+(y2-y1)**2)
    return round(dis,2)


def sum_distance(X,Y, dictionary):   #Defining a function which will give the distance between two points of the X and Y list.
    distan=[]  #Creates an empty list
    distances=0   # Since the intial distance travel is zero
    distan.append(distances)  # append will add up to the original list
    
    for i in range(len(X)-1):
        distances=distance(X[i],X[i+1],Y[i],Y[i+1])
        distan.append(distances)
        
    dictionary['Distance']=distan  # Adding the list of distance to the dictionary
 
sum_distance(dictionary[' X'],dictionary[' Y'],dictionary)   #Adding the george movement to dictionary
    
average_X=average_list(dictionary[' X'])  # Average X location movement
average_Y=average_list(dictionary[' Y'])  # Average Y location movement
average_energylevel=average_list(dictionary['Energy Level'])  #Average Energy level 
total_distance=sum_list(dictionary['Distance'])     #Calculating the total distance travelled

##
file=open("Georges_life.txt",'w')   #Creating an output file,w for writing it
## Writing file
#Creating header, s-string,f-float
file.write('Raccoon name: %s \n'%dictionary['Note'][:6])
file.write('Average location: x %f, Y %f \n'%(average_X,average_Y))
file.write('Distance travelled: %.2f \n' %total_distance)
file.write('Average Energy Level: %.2f \n' %average_energylevel)
file.write('Raccon end state: %s \n\n' %dictionary['Note'])  #\n\n indicates addition of 1 blank line in the file

head= ['Date','X','Y','Asleep Flag','Behaviour Mode','Distance Travelled']
file.write('%s \t %s \t %s \t %s \t %s \t %s \n'%(head[0],head[1],head[2],head[3],head[4],head[5]))

for i in range(len(dictionary['Year'])):
    file.write('%s \t %f \t %f \t %s \t %s \t %.2f \n'%(dictionary['Day'][i],dictionary[' X'][i],dictionary[' Y'][i],dictionary[' Asleep'][i],dictionary['Behavior Mode'][i],dictionary['Distance'][i]))
file.close()
