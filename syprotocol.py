from scapy.all import *
from time import sleep

for i in range(55,255):
    ippacket = IP()
    ippacket.dst='89.111.95.19'
    ippacket.ttl=i

    tcpcrap=TCP()
    tcpcrap.sport=4865
    tcpcrap.dport=5555
    tcpcrap.window=1212
    tcpcrap.flags="S"
    tcpcrap.options=[('WScale', 1), ('NOP', None)]

    data='USOM'
    whole=ippacket/tcpcrap/data
    
    for j in range(10):
        send(whole)
        sleep(10)
