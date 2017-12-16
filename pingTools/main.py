# -*- coding:utf8 -*-
from ping2 import *
import threading
import time
from apscheduler.schedulers.blocking import BlockingScheduler

#程序整体的调度器
def scheduler_main():
    scheduler = BlockingScheduler()
    scheduler.add_job(test, 'cron', second='*/10', hour='*')
    scheduler.add_job(test2, 'cron', second='*/10', hour='*')
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()

def test():
    LinkState('baidu.com')

def test2():
    LinkState('lol.com')

#线程函数
def action(arg,ip):
    num=0
    while(num<3600):  #执行n遍
        num=num+1
        time.sleep(1)
        print ip+'\n'
        LinkState(ip)
        time.sleep(1)



if __name__ == '__main__':
    #111.161.91.104 天津市联通 LOL游戏 端口号 58305
    #115.25.209.123 北京 Cerbet教育网 LOL游戏  端口号： 58309
    #b站播放视频   北京cernet 数据中心VIP通道  121.194.7.6
    ip=['taobao.com','jd.com','info.tsinghua.edu.cn','v.qq.com','bilibili.com','111.161.91.104','115.25.209.123','121.194.7.6'] #
    for i in range(8):
        t = threading.Thread(target=action, args=(i,ip[i]))
        t.start()

