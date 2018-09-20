#!/usr/bin/env python
#-*-coding: utf-8 -*-
"""
@version: 0.1
@author:linyl
@file: test_urllib2.py
@time: 2018/9/20 21:11
"""
import cookielib
import urllib2

url = "http://www.baidu.com"

print("第一种方法")

response1 = urllib2.urlopen(url)
print(response1.getcode())
print(len(response1.read()))

print("第二种方法")

request = urllib2.Request(url)
request.add_header("user-agent","Mozilla/5.0")
response2 = urllib2.urlopen(request)
print(response2.getcode())
print(len(response2.read()))

print("第三种方法")
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response3 = urllib2.urlopen(url)
print(response3.getcode())
print(response3.read())
print(cj)