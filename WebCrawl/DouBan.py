# _*_ coding=utf-8 _*_
import urllib.request
response = urllib.request.urlopen("https://www.baidu.com/")
print(response.read())