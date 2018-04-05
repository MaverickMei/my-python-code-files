#!/usr/bin/env python 
# -*- coding: utf-8 -*-
import jieba
from wordcloud import WordCloud #注意py文件名不能跟wordcloud重复，否则会出错！！
import matplotlib.pyplot as plt

f = open('000100.txt','rb')#读取二进制文件用rb
corpos = f.read()
seg_list = jieba.cut(corpos)#分词
text = " ".join(seg_list)
wordcloud = WordCloud(font_path="C:\\Windows\\Fonts\\simfang.ttf", background_color="white").generate(text)
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig("temp.jpg",dpi=200) #用反斜杠的话会报错
plt.show()

