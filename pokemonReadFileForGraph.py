# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 07:01:33 2016

@author: mdpitale
"""
import csv
import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.dates as mdates

dates=[]
android_avgRating_dates=[]
android_totalRating_dates=[]
android_size_dates=[]
android_data_avgRating=[]
android_data_totalRating=[]
android_data_size=[]
android_ratingScale_1=[]
android_ratingScale_2=[]
android_ratingScale_3=[]
android_ratingScale_4=[]
android_ratingScale_5=[]
android_ratingScale_date=[]

with open('android_data.csv','r') as f:
    lines = csv.reader(f)
    #print(lines)
    for line in lines:
        dates.append(line[0])
        if line[1] != '0':
            #print(type(line[1]))
            android_data_avgRating.append(line[1])
            android_avgRating_dates.append(line[0])
        if line[2] != '0':
            #print(type(line[1]))
            android_data_totalRating.append(line[2])
            android_totalRating_dates.append(line[0])
        if line[3] != '0':
            android_data_size.append(line[3])
            android_size_dates.append(line[0])
        rating_scale = [x.strip() for x in line[4].split(',')]
        #print(rating_scale)
        if rating_scale != ['0','0','0','0','0']:
            android_ratingScale_1.append(rating_scale[0])
            android_ratingScale_2.append(rating_scale[1])
            android_ratingScale_3.append(rating_scale[2])
            android_ratingScale_4.append(rating_scale[3])
            android_ratingScale_5.append(rating_scale[4])
            android_ratingScale_date.append(line[0])
x = [dt.datetime.strptime(d,'%Y_%m_%d %M_%S').date() for d in dates]
#print(x)
#For average Rating    
y = [float(i) for i in android_data_avgRating] 
x1 = [dt.datetime.strptime(d,'%Y_%m_%d %M_%S').date() for d in android_avgRating_dates] 
print("len x:",len(x1))
print("len y:",len(y))
#print("Y:",y)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y_%m_%d %M_%S'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=5))        
plt.plot(x1,y,label='Average Rating - Android')
plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0.)
plt.gcf().autofmt_xdate()
fig = plt.gcf()
fig.set_size_inches(20, 15.5, forward=True)
fig.savefig('androidAverageRating.png', dpi=100)

plt.clf()
    
#For total Rating    
y = android_data_totalRating 
x2 = [dt.datetime.strptime(d,'%Y_%m_%d %M_%S').date() for d in android_totalRating_dates] 
#print("Y:",len(y))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y_%m_%d %M_%S'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=5))        
plt.plot(x2,y, label='Total Rating - Android')
plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0.)
plt.gcf().autofmt_xdate()
fig = plt.gcf()
fig.set_size_inches(20, 15.5)
fig.savefig('androidTotalRating.png', dpi=100)

plt.clf()

#For size    
y = android_data_size
x3 = [dt.datetime.strptime(d,'%Y_%m_%d %M_%S').date() for d in android_size_dates]
#print("Y:",len(y))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y_%m_%d %M_%S'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=5))        
plt.plot(x3,y,label='Size - Android')
plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0.)
plt.gcf().autofmt_xdate()
fig = plt.gcf()
fig.set_size_inches(20, 15.5)
fig.savefig('androidSize.png', dpi=100)

plt.clf()

y = android_ratingScale_1
z = android_ratingScale_2
a = android_ratingScale_3
b = android_ratingScale_4
c = android_ratingScale_5
xx = [dt.datetime.strptime(d,'%Y_%m_%d %M_%S').date() for d in android_ratingScale_date]
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y_%m_%d %M_%S'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=5))
plt.plot(xx,y,label='Rating 1')
plt.plot(xx,z,label='Rating 2')
plt.plot(xx,a,label='Rating 3')
plt.plot(xx,b,label='Rating 4')
plt.plot(xx,c,label='Rating 5')
plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0.)
plt.gcf().autofmt_xdate()
fig = plt.gcf()
fig.set_size_inches(20, 15.5)
fig.savefig('androidRatingScale.png', dpi=100)

plt.clf()