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

reload(sys)
sys.setdefaultencoding('utf8')

#this fuction copy from : https://blog.csdn.net/FontThrone/article/details/72782499
def jiebaclearText(text):
    mywordlist = []
    seg_list = jieba.cut(text, cut_all=False)
    liststr="/ ".join(seg_list)
    f_stop = open(stopwords_path)
    try:
        f_stop_text = f_stop.read( )
        f_stop_text=unicode(f_stop_text,'utf-8')
    finally:
        f_stop.close( )
    f_stop_seg_list=f_stop_text.split('\n')
    for myword in liststr.split('/'):
        if not(myword.strip() in f_stop_seg_list) and len(myword.strip())>1:
            mywordlist.append(myword)
    return ''.join(mywordlist)
#copy end

if  __name__  == '__main__':
    #print(sys.argv)
    assert(len(sys.argv)==3 or len(sys.argv)==4)
    filename=sys.argv[1]
    assert(os.path.exists(filename))
    if len(sys.argv)==3:
        file_to_print_name=sys.argv[2]
        file_to_print=[]
    else:
        pos_file_to_print_name=sys.argv[2]
        neg_file_to_print_name=sys.argv[3]
        pos_file_to_print=[]
        neg_file_to_print=[]

    data=pd.read_csv(filename,encoding="utf-8")


    count =0

    for index, row in data.iterrows():
        string=""
        label=row["label"]
        if len(sys.argv)==3:
            records=json.loads(row["callback_content"])
            if 'result' not in records:
                continue
            record_result=records["result"]
        else:
            try:
                records=json.loads(row["records"].replace("\'", "\""))
                record_result=records
            except:
                print("wrong")
                print("")

        for rec in record_result:
            try:
                string=string+str(rec["type"])+" "+str(rec["detail"])+" "+str(rec["other"])+" "

            except Exception, e:
                continue
                # print 'str(Exception):\t', str(Exception)
                # print 'str(e):\t\t', str(e)
                # print 'repr(e):\t', repr(e)
                # print 'e.message:\t', e.message
                # print 'traceback.print_exc():'; traceback.print_exc()
                # print 'traceback.format_exc():\n%s' % traceback.format_exc()
                #
                # print(rec)
                # print(rec["type"])
                # print(rec["detail"])
                # print(rec["other"])
                # print("except")
                # exit()
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
        if len(sys.argv)==3:
            file_to_print.append(seg.encode("utf-8"))
        else:
            pos_file_to_print.append(seg.encode("utf-8"))
            neg_file_to_print.append(seg.encode("utf-8"))

    # for i in file_to_print:
    #     if type(i)!=str:
    #         print(i)
    #         print(type(i))
    #         break
    if len(sys.argv)==3:
        with open(file_to_print_name,"w") as f:
            f.writelines(file_to_print)
    else:
        with open(pos_file_to_print_name,"w") as f:
            f.writelines(pos_file_to_print)
        with open(neg_file_to_print_name,"w") as f:
            f.writelines(neg_file_to_print)
