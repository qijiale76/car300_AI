#!/usr/bin/python
# coding=utf-8

AUTHOR="齐家乐"

import sys
import json
import pandas as pd
import jieba
import os
import traceback
import math
import xlrd

stopwords_path="../../stopwords/哈工大停用词表.txt"

#this fuction copy from : https://blog.csdn.net/FontThrone/article/details/72782499
def jiebaclearText(text):
    mywordlist = []
    seg_list = jieba.cut(text, cut_all=False)
    liststr="/ ".join(seg_list)
    f_stop = open(stopwords_path)
    try:
        f_stop_text = f_stop.read( )
        f_stop_text=f_stop_text
    finally:
        f_stop.close( )
    f_stop_seg_list=f_stop_text.split('\n')
    for myword in liststr.split('/'):
        if not(myword.strip() in f_stop_seg_list) and len(myword.strip())>1:
            mywordlist.append(myword)
    return ''.join(mywordlist)
#copy end


def read_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

if  __name__  == '__main__':
    #assert(len(sys.argv)==4)
    #filename=sys.argv[1]
    #  assert(os.path.exists(filename))
    #pos_file_to_print_name=sys.argv[2]
    #neg_file_to_print_name=sys.argv[3]
    #pos_file_to_print=[]
    #neg_file_to_print=[]
    file_to_print_name='xlxd_exam.txt'
    file_to_print=[]

    count =0

    workbook = xlrd.open_workbook('维保记录分析是否事故车-上海曌扬5.26.xlsx')
    print(workbook.sheet_names())                  #查看所有sheet
    booksheet = workbook.sheet_by_index(0)         #用索引取第一个sheet
    for i in range(1000):
        x=booksheet.cell_value(i+1,5)
        #print(x)
        #exit()
        file_to_print.append("car_"+str(i)+'\n')
        try:
            x=json.loads(x)
        except:
            print('load_err')
            continue
       # label=y["label"]
        count=count+1
        print("\x1B[1A\x1B[K"+str(count))
        for y in x['result']:
            string=""
            try:
                string=string+str(y["type"])+" "+str(y["detail"])+" "+str(y["other"])+" "
            except:
                print('excpet')
                continue
            
            string = jiebaclearText(string)
            seg=string
            file_to_print.append(seg+'\n')

    with open(file_to_print_name,"w") as f:
        f.writelines(file_to_print)

