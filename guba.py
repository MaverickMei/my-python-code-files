#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# 代码来自http://blog.csdn.net/victordiao/article/details/52176400，有改动。
import urllib
import re  #导入对excel文件进行操作的库
import xlwt  #创建表格，设置编码模式，创建新的sheet

book=xlwt.Workbook(encoding='utf-8',style_compression=0)
sheet=book.add_sheet('dede',cell_overwrite_ok=True)
for j in range(1,1192):  #j的作用是对url不断进行修改，翻页,需要事先看好网页
    print (j)
    url = 'http://guba.eastmoney.com/list,600030,5,f_'+str(j)+'.html'
    try:
        request=urllib.request.Request(url)
        response=urllib.request.urlopen(request)
        content = response.read().decode('utf-8')
        pattern = re.compile('<span class.*?title=(.*?)>',re.S) #####（）里面就是提取的内容，.任意字符，*？匹配0或无数次+非贪婪模式
        title = re.findall(pattern, content)#符合正则的内容提取为列表，注意索引从0开始
        pattern = re.compile('<span class.*?<a href.*?data-popper.*?>(.*?)</a>', re.S)
        author = re.findall(pattern, content)
        pattern = re.compile('<span class.*?data-popper.*?</span><span class.*?>(.*?)</span>.*?<span class.*?>(.*?)</span>', re.S)
        time = re.findall(pattern, content)
        pattern = re.compile('<div class.*?articleh.*?<span.*?>(.*?)</span>.*?<span class.*?>(.*?)</span>', re.S)
        num = re.findall(pattern, content)
        for i in range(0,80): ####从列表中提取，每个列表80个元素，index为0-79
            titleans=title[i+1]
            sheet.write((j-1)*80+i,0,titleans)
            authorans=author[i]
            sheet.write((j - 1) * 80 + i, 1, authorans)
            fabiaotime=time[i][0]
            sheet.write((j - 1) * 80 + i, 2, fabiaotime)
            gengxintime=time[i][1]
            sheet.write((j - 1) * 80 + i, 3, gengxintime)
            yuedu = num[i][0]
            #print yuedu
            sheet.write((j - 1) * 80 + i, 4, yuedu)
            pinglun = num[i][1]
            #print pinglun
            sheet.write((j - 1) * 80 + i, 5, pinglun)
            #保存
            book.save('C:\\Users\\mcc\\Desktop\\Python Learning Notes\\600030.xls')

    except Exception as e:
                print("出错了")