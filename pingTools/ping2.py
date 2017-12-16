# -*- coding:utf8 -*-
#!/usr/bin/python
import requests,os,chardet
import subprocess
import re
from datetime import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf8')
def getUTF8(str):
    strEncode=chardet.detect(str)
    return str.decode(strEncode['encoding']).encode('utf8')

def getUnicode(str):
    strEncode=chardet.detect(str)
    return str.decode(strEncode['encoding'])

#将ping 的结果写入文件
def writeFile(str1,filename):
    f=file(filename,"a+")
    f.write('time: '+str(datetime.now())+"  ")
    for key,value in str1.items():
        f.write(key+":  "+ value +"  ")
    f.write('\n')
    f.close()

class LinkState(object):
    def __init__(self,ip):
        self.ip = ip
        self.getLinkState(self.ip)

    # 获取链路状态
    def getLinkState(self,ip):
        #运行ping程序
        p = subprocess.Popen(["ping.exe", ip],
             stdin = subprocess.PIPE,
             stdout = subprocess.PIPE,
             stderr = subprocess.PIPE,
             shell = True)

        #得到ping的结果
        out = p.stdout.read()
        #print getUnicode(out)

        #找出丢包率，这里通过‘%’匹配
        regex = re.compile(r'\w*%\w*')
        packetLossRateList = regex.findall(out)
        self.packetLossRate = packetLossRateList[0]

        #找出往返时间，这里通过‘ms’匹配
        regex = re.compile(r'\w*ms')
        timeList = regex.findall(out)
        self.minTime = timeList[-3]
        self.maxTime = timeList[-2]
        self.averageTime = timeList[-1]

        self.showResult()

    #输出结果
    def showResult(self):
        result = {'packetLossRate':self.packetLossRate,'minTime':self.minTime,'maxTime':self.maxTime,'averageTime':self.averageTime}
        print result
        #将结果保存在文件中
        writeFile(result,self.ip+'_pingResult.txt')



