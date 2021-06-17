import psutil
import socket
import time
from datetime import datetime


def getPrograms():
    
    packet = []

    for p in psutil.process_iter():
        packet.append(p.name())
    
    packet_str = repr(packet)
    return packet_str
    
def initServer():
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    s.bind(("192.168.0.92", 6677))

    print("Waiting for client...")

    s.listen(10)
    c, addr = s.accept()
    print('{} connected.'.format(addr))

    #data = packet_str
    
    i = 0
        
    while True:
    
        now = datetime.now()
        timeStamp = " ["+ now.strftime("%m/%d/%Y, %H:%M:%S" +"]")
    
        print("Sending packet "+ str(i) + timeStamp)
    
        packet = getPrograms()
    
        f = packet.encode()

        c.send(f)
        
        time.sleep(5)
        i+=1

    print("Done sending")
        

initServer()