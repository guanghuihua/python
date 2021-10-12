# _*_ coding:utf8 _*_
import os 
os.chdir(r"d:/pystudy/WebCrawl")
import urllib
import requests
import re 

turl='https://tieba.baidu.com/f?'
kw='上海对外经贸大学'
key=urllib.parse.urlencode({'kw':kw})   #这样做是为了解析中文，URL中是不能出现中文的
url=turl+key
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
    }
def webCrawl(url,headers):
    response=requests.get(url,headers=headers)
    response.encoding='UTF-8'
    data=response.text
    with open("htmltest.txt","w",encoding = "utf-8") as f:
        f.write(data)
    contentpat='<div class="threadlist_abs threadlist_abs_onlyline ">(.*?)</div>'  
    contentlist=re.compile(contentpat,re.S).findall(data)   #compile(pattern[, flags])可以创建 模式对象
    # .可以匹配除了换行符之外的所有字符，而re.S则可以影响. 使之能匹配换行符
    # .*? 可以匹配两边的所有字符，不过是非贪心模式
    with open("test.txt","w",encoding = "utf-8") as f:
        f.writelines(contentlist)


i=5
url = turl + key + "&ie=utf-8&pn=" + str((i-1)*50)
webCrawl(url,headers)
