# -*- coding:utf-8 -*-
# Author: owhileo
# Date: 2019-8-16
# Version: 1.0
import re

def pre_process(x):
    x=re.sub(r"[0-9a-zA-Z\- \*]+(?!柱)", "", str(x))
    x=re.sub(r"\s+|/|\*|■|▲|-|★|！|!|℃|=|●|\?|￥|\%|'|>|<", "", (x))#|[e-zE-Z0-9]
    x=re.sub(r"\.+|·",".", (x))
    x=re.sub(r";|；|：|@|\$|\#", ":", (x))
    x=re.sub(r'、|，',',',x)
    x=re.sub(r'\[|（|【','(',x)
    x=re.sub(r'\]|）|】',')',x)
    x=re.sub(r'\((,|\.)\)','',x)
    x=re.sub(r'(,\.)|(\.,)',',',x)
    x=re.sub(r',+',',',x)
    x=re.sub(r'(,|\.)\)',')',x)
    x=re.sub(r'\(\)','',x)
    x=re.sub(r"(,:)|(\.:)|(:\.)", ":", (x))
    x=re.sub(r":+", ":", (x))
    x=re.sub(r'_+','',x)
    x=re.sub(r'①|②|③|④|⑤|⑥|⑦|⑧|⑨|⑩|⑾|☆|¤|�|&','',x)
    
    return x
    
