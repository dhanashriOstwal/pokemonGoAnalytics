# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 07:01:17 2016

@author: mdpitale
"""
import os
from bs4 import BeautifulSoup
import codecs
import csv

def ios():
    date_list=[]
    ios_data_currVersion=[]
    ios_data_allVersion=[]
    ios_data_size=[]
    script_dir = os.path.dirname(__file__)
    rel_path = "pokemon_5378/data/"
    direct = os.path.join(script_dir, rel_path)
    for roots,dirs,files in os.walk(direct):    
        for name in files: 
            if name.endswith(("_ios.html")):
                cur_dir=roots + '/' + name
                print("Cur Dir: ",cur_dir)
                filename = name[0:5]
                d = cur_dir.split('/')
                date = ""                
                for item in d:
                    if "-" in item:
                        date = item
                        date=date.replace('-','_')  
                date_list.append(date + ' ' + filename)
                print("Date: ",date + ' ' + filename)
                f=codecs.open(cur_dir,"r","utf-8")
                soup=BeautifulSoup(f.read())
                rating = soup.find_all('span',{'class':'rating-count'})
                try:                
                    cur_version=rating[0].string.split(' ')[0]
                except:
                    cur_version=0
                try:
                    all_version=rating[1].string.split(' ')[0]
                except:
                    all_version=0
                lis=soup.find_all('ul',{'class':'list'})
                a=lis[0].find_all('li')
                size=a[4].text.split(':')[1][:-2]            
                desc=soup.find('p',{'itemprop':'description'})
                version=soup.find('span',{'itemprop':'softwareVersion'}).string
                print(cur_version)
                print(all_version)
                print(size)
                print(desc)
                print(version)
                ios_data_currVersion.append(cur_version)
                ios_data_allVersion.append(all_version)
                ios_data_size.append(size)
                details = [date + ' ' + filename,cur_version,all_version,size]
                f = open('ios_data.csv','a',newline='')
                data = csv.writer(f)                
                data.writerow(details)
                f.close()
                
def android():
    date_list=[]
    android_data_avgRating=[]
    android_data_totalRating=[]
    android_data_size=[]
    
    script_dir = os.path.dirname(__file__)
    rel_path = "pokemon_5378/data/"
    direct = os.path.join(script_dir, rel_path)
    for roots,dirs,files in os.walk(direct):    
        for name in files:     
            if name.endswith(("_android.html")):
                details = []
                android_ratingscale_list=[]
                android_ratingScale={}
                cur_dir=roots + '/' + name
                filename = name[0:5]
                d = cur_dir.split('/')
                date = ""                
                for item in d:
                    if "-" in item:
                        date = item
                        date=date.replace('-','_')  
                date_list.append(date + ' ' + filename)
                print("Date: ",date + ' ' + filename)
                f=codecs.open(cur_dir,"r","utf-8")
                soup=BeautifulSoup(f.read())
                try:
                    avg_rating=soup.find('div',{'class':'score'}).string
                    print("Average rating:",avg_rating)
                except:
                    avg_rating='0'
                try:
                    total_rating=soup.find('span',{'class':'reviews-num'}).string
                    print("Total rating:",total_rating)
                except:
                    total_rating='0'    
                rating_scale=soup.find_all('span',{'class':'bar-number'})
                for r in range(len(rating_scale)-1,-1,-1):
                    print("Rating scale:",r,rating_scale[r].string)
                    key = r
                    if key in android_ratingScale:
                        android_ratingScale[key].append(int(rating_scale[r].string.replace(',','')))
                    else:
                        android_ratingScale[key] = [int(rating_scale[r].string.replace(',',''))]
                try:
                    size=soup.find('div',{'itemprop':'fileSize'}).string
                    size = size.strip()[:-1]
                except:
                    size='0'
                try:
                    cur_version=soup.find('div',{'itemprop':'softwareVersion'}).string
                    print("Current version:",cur_version)
                except:
                    cur_version=0
                    print("Current version:",cur_version)
                desc=soup.find_all('div',{'jsname':'C4s9Ed'})
                print("Description:",desc)
                android_data_avgRating.append(avg_rating)
                android_data_totalRating.append(total_rating.replace(',',''))
                android_data_size.append(size)
                #print("Android Rating Scale: ", android_ratingScale)
                for key in android_ratingScale:
                    android_ratingscale_list.append(android_ratingScale.get(key)[0])
                android_ratingscale_list = str(android_ratingscale_list).replace('[','')
                android_ratingscale_list = str(android_ratingscale_list).replace(']','')
                #print("List:",android_ratingscale_list)
                
                details = [date + ' ' + filename,avg_rating,total_rating.replace(',',''),size,android_ratingscale_list]
                f = open('android_data.csv','a',newline='')
                data = csv.writer(f)                
                data.writerow(details)
                f.close()
                
#                           
ios()
android()