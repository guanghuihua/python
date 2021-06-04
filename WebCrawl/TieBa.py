# _*_ coding:utf8 _*_
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
response=requests.get(turl,headers=headers)
response.encoding='UTF-8'
data=response.text

contentpat='<div class="threadl(.*?)</div' 
# .可以匹配除了换行符之外的所有字符，而re.S则可以影响. 使之能匹配换行符
# .*? 可以匹配两边的所有字符，不过是非贪心模式
contentpat='<div class="threadlist_lz clearfix">(.*?)</div>'  
contentlist=re.compile(contentpat,re.S).findall(data)   #compile(pattern[, flags])可以创建 模式对象
print(len(contentlist))
for i in contentlist:
    print(i)






turl = 'https://mp.weixin.qq.com/cgi-bin/appmsg?t=media/appmsg_edit_v2&action=edit&isNew=1&type=10&createType=0&token=1393607498&lang=zh_CN'
turl = 'https://mp.weixin.qq.com/mp/jsmonitor?idkey=69271_78_1&t=0.784437322787632'
def webCrawl(turl):
    headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
    response=requests.get(turl,headers=headers)
    response.encoding='UTF-8'
    data=response.text
    contentpat='<section>(.*?)</section>' 
    # .可以匹配除了换行符之外的所有字符，而re.S则可以影响. 使之能匹配换行符
    # .*? 可以匹配两边的所有字符，不过是非贪心模式
    contentlist=re.compile(contentpat,re.S).findall(data)   #compile(pattern[, flags])可以创建 模式对象
    for i in contentlist:
        print(i)

webCrawl('https://mp.weixin.qq.com/s/1TinRoYgHZNDGwMt_1d9uA')
webCrawl('https://mp.weixin.qq.com/s/okQKyczeKQNAKXseZsXHUg')
webCrawl('https://mp.weixin.qq.com/s/ss4VoOrcVIs9jQdeosupNg')