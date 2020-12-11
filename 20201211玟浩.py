# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 09:30:57 2020

@author: user
"""

###############網頁擷取#################################
# import os
import requests
import time,datetime
# from datetime import datetime, timedelta
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
#################動態網頁########################################
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from lxml import etree
url="https://www.ettoday.net/news/news-list.htm"
options= webdriver.ChromeOptions()  #新增，略過網路憑證錯誤
options.add_argument('--ignore-certificate-errors') #新增，略過網路憑證錯誤
#options.add_argument('user-agent-{}'.format(headers)) #新增，略過網路憑證錯誤
driver=webdriver.Chrome(chrome_options=options) #新增，略過網路憑證錯誤
driver.get(url)
#############網頁擷取###########################################
r = requests.get("https://www.ettoday.net/news/news-list.htm")
r.encoding = "utf8"
###############################################################


now = datetime.datetime.now()
page=0
with open('玟浩.csv','w+',newline='', encoding="utf-8-sig") as csvfile:   #解決多一空行 newline=''
    import csv
    writer = csv.writer(csvfile)
    writer.writerow(('日期','分類','標題','連結'))
    

    for i in range(5):
        ################下拉####################
        for i in range(1,100):
            # driver.execute_script("window.scrollTo(0, ((document.body.scrollHeight)-10));")
            driver.execute_script("window.scrollTo(0,40749);")
            time.sleep(0.5)
    # ######################################
        # time_ago = datetime.now() - timedelta(hours = 24)
        # time_ago_time = time_ago.strftime("%Y/%m/%d %H:%M")
        # last_height = driver.execute_script("return document.body.scrollHeight")
        
        # go=True

        # while go:
        #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #     time.sleep(2)
        #     html_source = driver.page_source
        #     soup = BeautifulSoup(html_source, "lxml")
            
        #     new_height = driver.execute_script("return document.body.scrollHeight")

        #     #已經到頁面底部
        #     if new_height == last_height:
        #         print("已經到頁面最底部，程序停止")
        #         break

        #     last_height = new_height

        #     for d in soup.find(class_="part_list_2").find_all('h3'):
            
        #         if datetime.strptime(d.find(class_="date").text, '%Y/%m/%d %H:%M') < time_ago:
        #             print("已經超出"+hour+"個小時，程序停止")
        #             go = False
        #             break

        #         else:
        #             print("目前畫面最下方文章的日期時間為：",d.find_all(class_="date")[-1].text)
    ####################################################
        page+=1
        html = driver.page_source
        sp=BeautifulSoup(html,"html.parser")
        search_a=sp.select("div.part_list_2 > h3 > a")
        search_span=sp.select("div.part_list_2 > h3 > span")
        search_em=sp.select("div.part_list_2 > h3 > em")
        
        for i in range(len(search_a)):
            print(search_span[i].text,end=' ')
            print(search_em[i].text,end=' ')
            print(search_a[i].text,end=' ')
            print(search_a[i].get('href'))
            
            writer.writerow([search_span[i].text,search_em[i].text,search_a[i].text,search_a[i].get('href')])
        
        delta = datetime.timedelta(days=1)
        now= now-delta
        now1=now.strftime('%Y%m%d')
            
        d=now1[-2:]
        d=int(d)
        d=str(d)
            
        m=now1[-4:-2]
        m=int(m)
        m=str(m)
            
        driver.find_element_by_id("selM").click()
        Select(driver.find_element_by_id("selM")).select_by_visible_text(m)
        driver.find_element_by_id("selM").click()
        driver.find_element_by_id("selD").click()
        Select(driver.find_element_by_id("selD")).select_by_visible_text(d)
        driver.find_element_by_id("selD").click()
        driver.find_element_by_id("button").click()
         
        
    
    
    
        # driver.find_element_by_xpath("//a[@id='pnnext']/span[2]").click()
        # sleep(1)  # 必須加入等待，否則會有誤動作



driver.close()               #關閉瀏覽器


# sys.exit

