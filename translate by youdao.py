#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# 运用了延迟5秒提交和head伪装浏览器等解决反爬虫的措施
import urllib.request
import urllib.parse
import json
import time

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule" #去掉translate后面的_o可以破解其反爬虫机制
while True:
	content = input("请输入需要翻译的内容(输入quit即退出本程序！): ")
	if content == 'quit':
		break
	head = {} #head用于伪装成浏览器访问
	head['Referer'] = 'http://fanyi.youdao.com/'
	head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
	data = {}
	data['i'] = content
	data['from'] = 'AUTO'
	data['to'] = 'AUTO'
	data['smartresult'] = 'dict'
	data['client'] = 'fanyideskweb'
	data['doctype'] = 'json'
	data['version'] = '2.1'
	data['keyfrom'] = 'fanyi.web'
	data['action'] = 'FY_BY_REALTIME'
	data['typoResult'] = 'false'
	data = urllib.parse.urlencode(data).encode('utf-8') #关键步骤：给urlopen的data赋值就是post方式请求，data内部参数需要用urllib.parse.urlencode转换为application/x-www-from-urlencode格式
	req = urllib.request.Request(url, data, head) #将head传进去
	response = urllib.request.urlopen(req)
	html = response.read().decode('utf-8')
	target = json.loads(html)
	print("翻译结果：%s" % (target['translateResult'][0][0]['tgt']))
	time.sleep(5) #延迟5秒