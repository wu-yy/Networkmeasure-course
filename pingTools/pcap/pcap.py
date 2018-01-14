#coding:utf-8
#抽取IP地址进行域名反查
import requests
from bs4 import BeautifulSoup
import re
from pylab import *
import numpy as np
mpl.rcParams['font.sans-serif'] = ['SimHei']
import json

f=open('1.txt','r')
import matplotlib.pyplot as plt
r=f.readline()
data={'ip':[],'num':[],'name':[]}
name={}
while r:
    b=int(r.strip().split()[1])
    res=requests.get(url='http://ip.chinaz.com/?IP=%s'%r.strip().split()[0]) #解析ip反查域名地址
    soup=BeautifulSoup(res.content,"html.parser")
    try:
        addr= soup.find_all(name='p',class_='WhwtdWrap bor-b1s col-gray03')[0].text.strip().split('\n')[3]
        if name.has_key(addr):
            name[addr]=name[addr]+b
        else:
            name[addr]=b
    except:
        pass
    data['ip'].append(r.strip().split()[0])
    data['num'].append(r.strip().split()[1])
    r = f.readline()

import json
jdata= json.dumps(name, encoding="UTF-8", ensure_ascii=False)
name_list = []
num_list=[]
print name
for key ,value in name.items():
    name_list.append(key)
    num_list.append(int(value))

print num_list
x=range(len(num_list))
plt.bar(x, num_list,color='rgb',tick_label=name_list)
plt.xticks(x, name_list, rotation=90)
plt.show()
plt.savefig('show.jpg')