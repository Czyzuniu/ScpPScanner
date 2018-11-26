from scapy.all import *


def scan_port(port):
    status = 'OPEN'

    synPacket= sr1(IP(dst="23 192.168.3.0/24")/TCP(dport=(port), flags="S"))
    if (synPacket[TCP].flags != 18):
        status = 'CLOSED'
    
    print(synPacket.sprintf(str(port) + '\t %TCP.sport% \t %TCP.flags% ' + status))

    

scan_port(23)

