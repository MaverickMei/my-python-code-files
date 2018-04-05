#!/usr/bin/env python 
# -*- coding: utf-8 -*-
import requests
import json

def anjuke_linan(n):  #n为页码数量
    for i in range(1,n):
        url=(r'https://hangzhou.anjuke.com/sale/linanq/p'+str(i))
        headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
                  ':authority':'hangzhou.anjuke.com',
                  ':method':'GET',
                  ':scheme':'https',
                  'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                  'cookie':'aQQ_ajkguid=39ECB4CA-1D72-3408-C871-07F2ABC207BA; lps=http%3A%2F%2Fhangzhou.anjuke.com%2Fsale%2Flinanq%2Fp16%2F%7C; ctid=18; twe=2; sessid=9719C75C-8ACE-7AA5-ABC7-6AA35EDF592C; _ga=GA1.2.1934889245.1522508698; _gid=GA1.2.24748492.1522508698; 58tj_uuid=4be2a6b8-cafd-444d-8735-503af09124a4; init_refer=; new_uv=1; new_session=0; als=0; __xsptplus8=8.1.1522508697.1522508724.3%234%7C%7C%7C%7C%7C%23%23ayadoEKShAXnP09rb8NgYiy58fwUVw88%23',
                  'upgrade-insecure-requests':'1',
                  ':path':'/sale/linanq/p3/',
                  'referer':'https://hangzhou.anjuke.com/sale/linanq/p2/'}
        resp = requests.get(url=url,headers = headers )
        print (resp.text)

anjuke_linan(1)