# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 08:12:43 2020

@author: cis-user
"""
import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select

# r = requests.get("https://udn.com/news/story/7321/5018383?from=udn_ch2_menu_v2_main_index")
r = requests.get("https://www.cna.com.tw/news/firstnews/202011220165.aspx")
r.encoding = "utf8"

with open('html.text', "w", encoding="utf8") as fp:
    # print(r.text,file=fp)                                 ##可用print，也可用write
    fp.write(r.text)
    
with open('html.text', "r", encoding="utf8") as fp2:
    r2=fp2.read() 
    
page_source = r.text
page_source2 = page_source.split('\n')

soup = BeautifulSoup(r.text, "lxml")

####################################第一種#######################################
# tag_div=soup.find_all('div',class_="centralContent")
# print(tag_div)
# print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# for a in tag_div:
#     print(a.text)

# ####################################第二種#######################################

# tag_div1=soup.find_all('div',class_="scrollable")
# print(tag_div1)
# print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# for a in tag_div1:
#     print(a.text)

# ####################################第三種#######################################
# tag_div2=soup.find_all('div',class_="page--index")
# print(tag_div2)
# print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# for a in tag_div2:
#     print(a.text)
####################################第四種#######################################
tag_div3=soup.find_all('div',class_="paragraph")
print(tag_div3)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
for a in tag_div3:
    print(a.text)
    
    
# import csv
# with open('1.csv','w',newline='' )as csvfile:
#     wt=csv.writer(csvfile)
#     wt.writerow([tag_div,tag_div1,tag_div2,tag_div3])