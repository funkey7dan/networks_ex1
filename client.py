from socket import socket,AF_INET,SOCK_DGRAM
import sys

BUFFER = 95
IP = sys.argv[1]
PORT = int(sys.argv[2])
file_name = sys.argv[3]
file = open(file_name,mode = 'rb')
s = socket(AF_INET,SOCK_DGRAM)
s.settimeout(1)

bytes = file.read(BUFFER)
index = 0
while bytes:
    s.sendto(str(index).encode()+b'_'+bytes,(IP,PORT))
    #print("sent\n" + str(index)+'_'+ bytes.decode())
    received_bool = False
    while not received_bool:
        try:
            data,addr = s.recvfrom(BUFFER)
            #print("received:\n"+data.decode())
            if data.decode() == str(index):
                received_bool = True
                index += 1
                bytes = file.read(BUFFER)
        except:
            s.sendto(str(index).encode()+b'_'+bytes,(IP,PORT))
            #print("sent\n"+str(index)+bytes.decode())

file.close()
s.close()
exit(0)
