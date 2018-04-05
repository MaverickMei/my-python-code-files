#增加list元素
classmates.append('Adam')
>>> classmates
['Michael', 'Bob', 'Tracy', 'Adam']

#插入到指定索引
>>> classmates.insert(1, 'Jack')
>>> classmates
['Michael', 'Jack', 'Bob', 'Tracy', 'Adam']

#删除末尾元素
>>> classmates.pop()
'Adam'
>>> classmates
['Michael', 'Jack', 'Bob', 'Tracy']

#删除指定索引元素
>>> classmates.pop(1)
'Jack'
>>> classmates
['Michael', 'Bob', 'Tracy']

#替换指定索引元素
>>> classmates[1] = 'Sarah'
>>> classmates
['Michael', 'Sarah', 'Tracy']

list里面的元素的数据类型也可以不同，list元素也可以是另一个list
 s = ['python', 'java', ['asp', 'php'], 'scheme']
s[2][1]='php' #二维数组

classmates = ('Michael', 'Bob', 'Tracy')
#tuple数组不可变，代码更安全 t = (1,)


weight=45
height=163
print('您的体重=',weight,'您的身高=',height)
bmi = weight/(height*height)
print('BMI指数:\n低于18.5:过轻\n18.5-25:正常\n25-28:过重\n28-32:肥胖\n高于32:严重肥胖')
print('您的bmi=',bmi)
if bmi<18.5:
    print('体重过轻！')
elif bmi<25:
    print('正常')
elif bmi<28:
    print('体重过重！')
elif bmi<32:
    print('体重肥胖！')
else:
    print('严重肥胖！')

	
dir(__builtins__)#内置函数列表



#2018.1.11 learning

#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# if __name__ == "__main__": 解决的问题：模块被单纯调用。
# 集成开发环境（IDE）的选择：cmd、自带的IDLE以及第三方软件（Notepad++等等） 在Notepad++中启动python需设置路径和快捷键：cmd /k python "$(FULL_CURRENT_PATH)" & PAUSE & EXIT 
# 文件的打开相关
f=open("txt.txt")  #python根目录下 打开模式：只读'r',写入'w'
	f.read()
	f.tell()      #指针位置 f.seek(offset,from)调整 from 0起始 1当前 2文末
	f.readline()  #读到换行符\n截止
	list(f)       #
	for each_line f
		print (each_line) #文件对象支持迭代
#'w'模式下，对文件进行写入操作
f.write("\n写入内容") #该模式下进行了文本内容的替代 'a'模式下进行追加写入
f.close()
#通配符相关  通常在正则表达式中应用广泛  反斜杠\+元字符可抵消
#	（.）匹配换行符以外的任意字符
#	（?）匹配一个字符
#	（*）匹配任意多字符
#等等

#2018.1.12 learning
#代码缩进会影响逻辑！！
#解决反爬虫的几个方法：增加head参数、延迟提交数据、使用代理

#2018.1.13 learning
#加r前缀可以使其成为普通字符，避免元字符和转义的影响
    print(r'\n\\')
    print('\n\\')
#正则表达式学习
    re.search(r'ao梅', 'meichengchao梅成超是个好人.')
    #result：<_sre.SRE_Match object; span=(10, 13), match='ao梅'>
    #（.）通配符，=可以匹配除了换行符以外的任何字符
    #如果只想匹配该字符本身，则利用反斜杠转义掉：
    re.search(r'\.', 'meichengchao梅成超是个好人.')
#字符类
    re.search(r'[aeiouAEIOU]', '')#匹配d大小写元音字母
    re.search(r'[a-z][A-Z]', '')
    re.search(r'[a-z]', '')
    re.search(r'[0-2][0-5][0-5]', '') #255
#匹配次数   +一次或者多次，*零次或多次，？零次或一次
    re.search(r'ab{3}c', 'abbbc')
    re.search(r'ab{3,5}c', 'abbbbc')
#正则表达式只匹配0-9.（字符串）
    re.search(r'(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])', 'abbbc255.255.255.255')
    #5.25.255.255
#正则表达式不能随意用空格
#贪婪模式：
    re.search('<.+>','<html><><>')
    #匹配结果为：<html><><>而不是<html>
    re.search('<.+?>','<html><><>')#关闭贪婪模式
#重复使用某一正则表达式：编译
    p = re.compile("A-Z")
    p.search("AzzzFaA")
    p.findall("AzzzFaA")
    #编译标志相关
#re.search 提取对象内容
    result=re.search('aaa','AAAaaaAAA')
    result.group()#匹配的字符串
    result.start()#4
    result.end()#6
    result.span()#(4,6)






