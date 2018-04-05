#!/usr/bin/env python 
# -*- coding: utf-8 -*-
import urllib.request
import re
import os

response = urllib.request.urlopen("http://tieba.baidu.com/p/3823765471")
html = response.read().decode("utf-8")
p = r'BDE_Image".src="([^"]*\.jpg)".*?>'#用括号括起提取内容，find可以直接得到该部分
imglist = re.findall(p, html)
try:
    os.mkdir("Pics")#创建单层目录（在当前工作目录下）
except FileExistsError:
    pass#如果该文件夹存在则覆盖
os.chdir("Pics")#改变工作目录
for each in imglist:
    filename = each.split("/")[-1]#网址最后一级域名.jpg
    urllib.request.urlretrieve(each, filename, None)


