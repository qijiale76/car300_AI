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

stopwords_path="../stopwords/哈工大停用词表.txt"

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
    assert(len(sys.argv)==4)
    filename=sys.argv[1]
    assert(os.path.exists(filename))
    pos_file_to_print_name=sys.argv[2]
    neg_file_to_print_name=sys.argv[3]
    pos_file_to_print=[]
    neg_file_to_print=[]

    data = read_json(filename)

    count =0

    for x in data:
        for y in x['records']:
            string=""
            label=y["label"]
            try:
                string=string+str(y["type"])+" "+str(y["detail"])+" "+str(y["other"])+" "
            except:
                continue
            if (count % 100)==0:
                print("\x1B[1A\x1B[K"+str(count))
            string = jiebaclearText(string)
            count=count+1
            if label==1:
                print_label="  __label__1\n"
            elif label==0:
                print_label="  __label__0\n"
            else:
                print('wrong label'+str(label))
                continue
            seg=string+print_label
            if label==1:
                pos_file_to_print.append(seg)
            elif label==0:
                neg_file_to_print.append(seg)

    with open(pos_file_to_print_name,"w") as f:
        f.writelines(pos_file_to_print)
    with open(neg_file_to_print_name,"w") as f:
        f.writelines(neg_file_to_print)
