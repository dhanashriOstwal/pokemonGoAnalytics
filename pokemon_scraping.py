# -*- coding: utf-8 -*-
"""
Created on Sun Dec 04 16:42:04 2016

@author: saranya
"""
import os
from bs4 import BeautifulSoup
import codecs
import matplotlib.pyplot as plt
import collections
import json

def ios():
    script_dir = os.path.dirname(__file__)
    rel_path = "pokemon_5378/data/"
    direct = os.path.join(script_dir, rel_path)
    ios_dict=collections.defaultdict(dict)
    for roots,dirs,files in os.walk(direct):    
        for name in files:     
            if name.endswith(("_ios.html")):
                cur_dir=roots + '/' + name
                date= cur_dir.split('/')[5]+'_'+cur_dir.split('/')[6].split('_')[0]+'_'+cur_dir.split('/')[6].split('_')[1]
                date=date.replace('-','_')            
                #print(date)
                f=codecs.open(cur_dir,"r","utf-8")
                soup=BeautifulSoup(f.read(),"lxml")
                #cur_version = soup.find('span',{'class':'rating-count'}).string
                rating = soup.find_all('span',{'class':'rating-count'})
                try:                
                    cur_version=rating[0].string.split(' ')[0].encode('utf-8')
                except:
                    cur_version=0
                ios_dict[date]['total_rating_current_version']=cur_version
                try:
                    all_version=rating[1].string.split(' ')[0].encode('utf-8')
                except:
                    all_version=0
                ios_dict[date]['total_rating']=all_version
                lis=soup.find_all('ul',{'class':'list'})
                a=lis[0].find_all('li')
                size=a[4].text.split(':')[1][:-2]
                ios_dict[date]['file_size']=size.encode('utf-8')
                desc=soup.find('p',{'itemprop':'description'}).getText().encode('utf-8')
                desc=unicode(desc,'ascii','ignore')
                ios_dict[date]['description']=desc.encode('utf-8')
                version=soup.find('span',{'itemprop':'softwareVersion'}).string
                ios_dict[date]['version']=version.encode('utf-8')
    with open('pokemon_ios.json','w') as wf:
        json.dump(ios_dict,wf,sort_keys=True,indent=4)          
                
def android():
    script_dir = os.path.dirname(__file__)
    rel_path = "pokemon_5378/data/"
    direct = os.path.join(script_dir, rel_path)
    android_dict=collections.defaultdict(dict)
    for roots,dirs,files in os.walk(direct):    
        for name in files:     
            if name.endswith(("_android.html")):
                cur_dir=roots + '/' + name
                date= cur_dir.split('/')[5]+'_'+cur_dir.split('/')[6].split('_')[0]+'_'+cur_dir.split('/')[6].split('_')[1]
                date=date.replace('-','_')
                
                f=codecs.open(cur_dir,"r","utf-8")
                soup=BeautifulSoup(f.read(),"lxml")
                try:
                    avg_rating=soup.find('div',{'class':'score'}).string.encode('utf-8')
                    #print(avg_rating)
                except:
                    avg_rating=0
                android_dict[date]['average_rating']=avg_rating
                try:
                    total_rating=soup.find('span',{'class':'reviews-num'}).string.encode('utf-8')
                    #print(total_rating)
                except:
                    total_rating=0
                android_dict[date]['total_rating']=total_rating
                rating_scale=soup.find_all('span',{'class':'bar-number'})
                for r in range(len(rating_scale)-1,-1,-1):
                    col_name='rating_'+str(len(rating_scale)-r)
                    android_dict[date][col_name]=rating_scale[r].string.encode('utf-8')
                try:
                    size=soup.find('div',{'itemprop':'fileSize'}).string.strip()[:-1].encode('utf-8')
                    
                except:
                    size=0
                android_dict[date]['file_size']=size
                try:
                    cur_version=soup.find('div',{'itemprop':'softwareVersion'}).string.encode('utf-8')
                    #print(cur_version)
                except:
                    cur_version=0
                android_dict[date]['version']=cur_version
                desc=soup.find('div',{'jsname':'C4s9Ed'}).getText().encode('utf-8')
                desc=unicode(desc,'ascii','ignore')                
                android_dict[date]['description']=desc.encode('utf-8')
    with open('pokemon_android.json','w') as wf1:
        json.dump(android_dict,wf1,sort_keys=True,indent=4)            
                                
ios()
android()