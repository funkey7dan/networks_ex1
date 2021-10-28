import socket
import sys
IP = "10.0.2.4"
PORT = int(sys.argv[1])
BUFFER = 100

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('',PORT))

while True:
    data,addr = s.recvfrom(BUFFER)
    if data.decode() == 'received':
        #print("Sent yes")
        s.sendto(b'yes',addr)
    else:
        print(str(data.decode('utf8')))
    s.sendto(data,addr)
