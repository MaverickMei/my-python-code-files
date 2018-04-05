#!/usr/bin/env python 
# -*- coding: utf-8 -*-
import xlrd

def strs(row):
    values = ""
    # for i in range(len(row)):
    #     alues = values + str(row[i])
    # return values
    for i in range(len(row)):
        if i == len(row) - 1:
            values = values + str(row[i])
        else:
            values = values + str(row[i]) + ","
    return values


data = xlrd.open_workbook("000725.xls")
textfile = open("000725.txt", "w") # 文件读写方式是
table = data.sheets()[0] # 表头
nrows = table.nrows  # 行数
ncols = table.ncols  # 列数
row_data = table.row_values(0)  # 第一行数据
column_data = table.col_values(0) #第一列数据
text = " ".join(column_data)
#print (text)
textfile.write(text) #将字符串写入新文件
textfile.close() # 关闭写入的文件

#把第一列提取转化为txt：
# col = table.col_values(0)
# values = strs(col)
# textfile.writelines(values + "\r") #将字符串写入新文件
# textfile.close() # 关闭写入的文件

#把所有数据拼接成txt：
# for ronum in range(1, nrows):
#     row = table.row_values(ronum)
#     values = strs(row) # 条用函数，将行数据拼接成字符串
#     textfile.writelines(values + "\r") #将字符串写入新文
# textfile.close() # 关闭写入的文件