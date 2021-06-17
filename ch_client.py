import socket
from datetime import datetime


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.0.92", 6677))

f = open("programs.txt", "wb")

print("Connected to server")

i = 0

while True:
    datas = s.recv(4096)
    while datas:
        now = datetime.now()
        timeStamp = " [" + now.strftime("%d/%m/%Y %H:%M:%S") +"]"

        f.write(timeStamp)
        f.write("\n\n")
        f.write(datas)
        f.write("\n\n")

        
        datas = s.recv(4096)
        print("Received packet " + str(i) + timeStamp)
        
        i+=1
    f.close()
    break
print("Transfer terminated by server")