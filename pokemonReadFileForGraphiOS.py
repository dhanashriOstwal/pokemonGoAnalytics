# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 21:05:43 2016

@author: mdpitale
"""
import csv
import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.dates as mdates
dates = []
dates_allVersion=[]
dates_currVersion=[]
ios_data_currVersion=[]
ios_data_allVersion=[]
ios_data_size=[]
with open('ios_data.csv','r') as f:
    lines = csv.reader(f)
    #print(lines)
    for line in lines:
        dates.append(line[0])
        if line[1] != '0':
            ios_data_currVersion.append(line[1])
            dates_currVersion.append(line[0])
        if line[2] != '0':
            dates_allVersion.append(line[0])
            ios_data_allVersion.append(line[2])
        ios_data_size.append(line[3])
        
x = [dt.datetime.strptime(d,'%Y_%m_%d %M_%S').date() for d in dates]
    
    #For current Version Rating 
a = [dt.datetime.strptime(d,'%Y_%m_%d %M_%S').date() for d in dates_currVersion]
y = ios_data_currVersion  
print("Y:",len(y))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y_%m_%d %M_%S'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=5))        
plt.plot(x,y,label = 'Current Version Rating - iOS')
plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0.)
plt.gcf().autofmt_xdate()
fig = plt.gcf()
fig.set_size_inches(20, 15.5)
fig.savefig('iosCurrentVersion.png', dpi=100)

plt.clf()                     
#For all Version Rating    
print(ios_data_allVersion)
b = ios_data_allVersion
c = [dt.datetime.strptime(d,'%Y_%m_%d %M_%S').date() for d in dates_allVersion]
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y_%m_%d %M_%S'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=5))        
plt.plot(c,b, label='All Version Rating - iOS')
plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0.)
plt.gcf().autofmt_xdate()
fig2 = plt.gcf()
fig2.set_size_inches(20, 15.5)
fig2.savefig('iosAllVersion.png', dpi=100)

plt.clf()
#    #For size 
#    
d = ios_data_size
f = plt.figure(1)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y_%m_%d %M_%S'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=5))        
plt.plot(x,d,label='Size - iOS')
plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0.)
plt.gcf().autofmt_xdate()
fig = plt.gcf()
fig.set_size_inches(20, 15.5)
fig.savefig('iosSize.png', dpi=100)