#!/usr/bin/env python

import os
import pandas as pd
import urllib.request
import realprice_key as key
from requests import get
from bs4 import BeautifulSoup

import csv

api_key = key.api_key
ymd = '202002'
landcode = '11170'

url ="http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTrade?serviceKey=" + api_key + "&LAWD_CD=" + landcode + "&DEAL_YMD=" + ymd 



def main():
    res = urllib.request.urlopen(url)
    result = res.read()
    soup = BeautifulSoup(result,'lxml-xml')
    items = soup.findAll("item")

    rp = pd.DataFrame(
        {"건축년도" : [],
         "년" : [],
         "월" : [],
         "일" : [],
         "법정동" : [],
         "거래금액" :[],
         "전용면적" : [],
         "지번": [],
         "층": []})
    
    for i in items:
        b_year = i.find("건축년도").text
        t_year = i.find("년").text
        t_month = i.find("월").text
        t_day = i.find("일").text
        dong = i.find("법정동").text
        price = i.find("거래금액").text
        area = i.find("전용면적").text
        jb = i.find("지번").text
        flr = i.find("층").text
        
        #rp.loc[i] =[b_year]+[t_year]+[t_month]+[t_day]+[dong]+[price]+[area]+[jb]+[flr] 
        #print(rp)

        temp = pd.DataFrame(
            {"건축년도" : [b_year],
             "년" : [t_year],
             "월" : [t_month],
             "일" : [t_day],
             "법정동" : [t_day],
             "거래금액" :[dong],
             "전용면적" : [price],
             "지번": [jb],
             "층": [flr]})

        #temp = pd.DataFrame(b_year,t_year,t_month,t_day,dong,price,area,jb,flr])
        #print(temp)
        rp = rp.append(temp)

        
    print(rp)
    rp.to_csv("realprcie.csv",mode="w", encoding="cp949")


if __name__ =="__main__":
    main()

