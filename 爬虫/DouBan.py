# _*_ coding=utf-8 _*_
import urllib.request  #制定URL，获取网页数据
import requests
from bs4 import BeautifulSoup  #网页解析，获取数据
import re 
import xlwt  #进行excel进行操作
import sqlite3  #进行SQLite进行数据库操作


def main():
    baseurl = "https://movie.douban.com/top250?start="
    # 1. 爬取网页
    datalist = getData(baseurl)
    savepath = r"d:/pystudy/WebCrawl"
    # 3. 保存数据
    saveData(savepath)



# 爬取网页
def getData(baseurl):
    datalist = []
    
    # 2. 逐一解析数据
    return datalist 



#  保存数据
def saveData(savepath):
    print(saveData)



if __name__ == "__main__":
    main()

    
