# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import matplotlib as mpl
import os
import time
import re
def drawLine():
    file_path=get_path('./')
    label=[]
    minVec=[]
    maxVec=[]
    averageVec=[]
    color=['red','pink','green','blue','yellow','orangered','m','black']
    marker=['o','D','+','*','d','p','>','>']
    for item in file_path:
        min,max,average=dofile(item)
        minVec.append(min)
        maxVec.append(max)
        averageVec.append(average)
        label.append(item[:-15])

    #画最小的时间间隔
    for i in range(len(minVec)):
        Larray=minVec[i]
        x = range(len(minVec[i]))
        plt.plot(x, Larray, label=label[i], linewidth=0.1, color=color[i%8], marker=marker[i%8], markerfacecolor=color[i%8], markersize=1)
        plt.xlabel('time/5s')
    plt.ylabel('minTime')
    plt.title('2017-12-16 03:25:23-08:29:18')
    plt.legend()
    file = 'minTime.png'
    plt.savefig(file)
    plt.close()

    # 画最大的时间间隔
    for i in range(len(maxVec)):
        Larray = maxVec[i]
        x = range(len(maxVec[i]))
        plt.plot(x, Larray, label=label[i], linewidth=0.1, color=color[i % 8], marker=marker[i%8], markerfacecolor=color[i % 8],
                 markersize=1)
        plt.xlabel('time/5s')
    plt.ylabel('maxTime')
    plt.title('2017-12-19 12:00:00-17:30:18')
    plt.legend()
    file = 'maxTime.png'
    plt.savefig(file)
    plt.close()
    # plt.show()

    # 画平均的时间间隔
    for i in range(len(averageVec)):
        Larray = averageVec[i]
        x = range(len(averageVec[i]))
        plt.plot(x, Larray, label=label[i], linewidth=0.1, color=color[i % 8], marker=marker[i%8], markerfacecolor=color[i % 8],
                 markersize=1)
        plt.xlabel('time/5s')
    plt.ylabel('averageTime')
    plt.title('2017-12-16 03:25:23-08:29:18')
    plt.legend()
    file = 'averageTime.png'
    plt.savefig(file)
    plt.close()
    # plt.show()

#解析文件内容，找到ping的数值
def dofile(filename):
    f=open(filename,'r')
    line=f.readline()
    num=0
    min=[]
    max=[]
    average=[]
    while(line and num<12):
        str=line
        minTime = int(re.compile('minTime:\s*(\d*)ms').findall(str)[0])
        maxTime = int(re.compile('maxTime:\s*(\d*)ms').findall(str)[0])
        averageTime = int(re.compile('averageTime:\s*(\d*)ms').findall(str)[0])
        min.append(minTime)
        max.append(maxTime)
        average.append(averageTime)
        line=f.readline()
    return min,max,average


#获取文件下面的所有文件
def get_path(path):
    #return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('Result.txt')]
    return [f for f in os.listdir(path) if f.endswith('Result.txt')]

if __name__=="__main__":
    drawLine()
    #print(time.strftime("%Y-%m-%d-%X", time.localtime()))