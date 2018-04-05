#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
#将复杂的数据文件另存为二进制文件，并从二进制文件重新恢复为原来的数据文件
import pickle

my_list = [111, 3.14, 'www', ['another list']]
pickle_file = open(r"C:\Users\mcc\Desktop\Python Learning Notes\pickle_excel.pkl",'wb') #注意打开模式，覆盖写入/二进制打开
pickle.dump(my_list,pickle_file)
pickle_file.close()

pickle_file = open(r"C:\Users\mcc\Desktop\Python Learning Notes\pickle_excel.pkl",'rb') #只读/二进制打开
my_list = pickle.load(pickle_file)
print(my_list)

